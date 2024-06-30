import pandas as pd
from DataPreprocessor import DataPreprocessor

class DataLoader:
    "Splits data into training and test sets"
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.load_data()
        self.train_data, self.test_data = self.split_data()

    def load_data(self):
        print("Loading data")
        preprocessor = DataPreprocessor(self.data_path)
        data = preprocessor.process_data()
        return data
        
    def split_data(self):
        
        # Convert to datatime
        df = self.data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        print("Splitting data into training and testing sets")
        # Split into training and testing sets
        train_data = df[(df['timestamp'] >= '2018-04-01') & (df['timestamp'] <= "2018-06-30")]
        test_data = df[(df['timestamp'] >= "2018-07-01") & (df['timestamp'] <= "2018-08-31")]
        
        print("\tTraining data shape:", train_data.shape)
        print("\tTesting data shape:", test_data.shape)
    
        # save data
        train_data.to_csv('Data/train_data.csv', index=False)
        test_data.to_csv('Data/test_data.csv', index=False)
        
        return train_data, test_data
