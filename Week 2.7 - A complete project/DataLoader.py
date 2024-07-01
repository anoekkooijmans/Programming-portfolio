import pandas as pd
import json

class DataLoader:
    "Splits data into training and test sets"
    def __init__(self, filename, config="application.json"):
        with open(config) as f:
            config = json.load(f)
        self.input_dir = config["input_directory"] 
        self.data_path = self.input_dir + "/" + filename
        self.data = pd.read_csv(self.data_path).drop('Unnamed: 0', axis=1)
        self.train_data, self.test_data = self.split_data()

    def split_data(self):        
        # Convert to datatime
        df = self.data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Split into training and testing sets
        train_data = df[(df['timestamp'] >= '2018-04-01') & (df['timestamp'] <= "2018-06-30")]
        test_data = df[(df['timestamp'] >= "2018-07-01") & (df['timestamp'] <= "2018-08-31")]
        
        print('-' * 100)
        print("Training data shape:", train_data.shape)
        print("Testing data shape:", test_data.shape)
        print('-' * 100)
        
        # Save data
        train_data.to_csv(f'{self.input_dir}/processed/train_data.csv', index=False)
        test_data.to_csv(f'{self.input_dir}/test_data.csv', index=False)
        
        return train_data, test_data

