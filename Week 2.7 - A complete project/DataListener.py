import json
import os
import shutil
import pandas as pd
import joblib
import time
from datetime import datetime
from DataPreprocessor import DataPreprocessor
from DataTrainer import TrainModel
from DataPlotter import DataPlotter

class DataListener:
    """"
    Checks input directory for new files. 
    Once they are found they are fitted to the trained machine learning model.
    The transformed data is then saved and file is moved to the "processed" folder.
    """
    def __init__(self,config="application.json"):
        with open(config) as f:
            config = json.load(f)
            
        self.input_dir = config["input_directory"]
        self.output_dir = config["output_directory"]
        self.img_dir = config["img_directory"]
        self.sensor_names = config["sensor_names"]
        self.check_interval_seconds = config["check_interval_seconds"]
        self.model = TrainModel()  
        self.preprocessor = DataPreprocessor() 
        self.plotter = DataPlotter()
        
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("application.log", "a") as log_file:
            log_file.write(f"{timestamp}  {message}\n")
        
    def listen(self):
        while True:
            self.check_for_new_data()
            time.sleep(self.check_interval_seconds) 
            
    def check_for_new_data(self):
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".csv"):
                self.log(f"Found new data file: {filename}")
                self.process_data(filename)
                break
                
    def data_check(self,df):        
        required_columns = ['timestamp'] + self.sensor_names + ['machine_status']
        return set(required_columns).issubset(list(df.columns))
    
    def fit_data(self,algorithm,X,df):
        y_pred = algorithm.fit(X).predict(X)

        print('-' * 100)
        print("Isolation Forest")
        print("Number of anomolies detected:")
        print(pd.Series(y_pred).value_counts())
        print('-' * 100)     
        
        df["Isolation Forest"] = y_pred
        return df
             
    def process_data(self, filename):
        self.log(f"Loaded the file: {filename}")
        file_path = os.path.join(self.input_dir, filename)
        df = pd.read_csv(file_path)
        
        if self.data_check(df):
            X = self.preprocessor.process_data(df)
            self.log("Received transformed data")
            
            # Load trained model
            model = joblib.load(f"{self.output_dir}/isolation_forest_model.joblib")
            algorithm = model.fit(X)
            df = self.fit_data(algorithm,X,df)
            df['timestamp'] = pd.to_datetime(df['timestamp'])

            
            self.log("Received predictions")
            
            output_path = os.path.join(self.output_dir, f"transformed_{filename}")
            df.to_csv(output_path, index=False)
            self.log(f"Saving predictions to: {output_path}")
            
            for sensor in self.sensor_names:
                plt = self.plotter.plot_sensor_anomolies(df,sensor)
                img_name = f"{df['timestamp'].iloc[0].strftime('%Y-%m')}-{sensor}.png"
                img_path = img_path = os.path.join(self.img_dir, img_name)
                plt.savefig(img_path)
                self.log(f"Saving image: {img_path}")
            
            PATH = f"{self.input_dir}/processed"
            if not os.path.exists(PATH):
                os.mkdir(PATH)    
            shutil.move(file_path, os.path.join(self.input_dir, "processed", filename))
            
            self.log("Resuming listening")
            
        else:
            self.log(f"Error: File {filename} does not contain the timestamp, sensor names or machine status column")        
        