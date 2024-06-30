import pandas as pd 
from sklearn.ensemble import IsolationForest
import joblib
from DataPreprocessor import DataPreprocessor

class TrainModel:
    
    def __init__(self,data_path):
        self.data_path = data_path
        self.preprocessor = DataPreprocessor(self.data_path)
        self.data = self.preprocessor.data
        self.X = self.preprocessor.process_data()
        self.trained_data = self.train_model()
    
    def train_model(self):
        normal_rows = self.data[self.data['machine_status'] == 'NORMAL']
        outliers_fraction = 1 - (len(normal_rows) / len(self.data))
        
        print("\nTraining model")
        algorithm = IsolationForest(contamination=outliers_fraction, n_jobs = -1)
        y_pred = algorithm.fit(self.X).predict(self.X)
        
        print('-' * 100)
        print("Isolation Forest")
        print("Number of anomolies detected:")
        print(pd.Series(y_pred).value_counts())
        print('-' * 100)        
        
        joblib.dump(algorithm, 'Data/isolation_forest_model.joblib')
        
        self.data["Isolation Forest"] = y_pred
        
        return self.data
        

    
        
    
        
