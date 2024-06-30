import pandas as pd

class DataLoader:
    "Splits data into training and test sets"
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path).drop('Unnamed: 0', axis=1)
        self.train_data, self.test_data = self.split_data()

    def split_data(self):
        print("\nLoading data")
        
        # Convert to datatime
        df = self.data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        print("\nSplitting data into training and testing sets")
        # Split into training and testing sets
        train_data = df[(df['timestamp'] >= '2018-04-01') & (df['timestamp'] <= "2018-06-30")]
        test_data = df[(df['timestamp'] >= "2018-07-01") & (df['timestamp'] <= "2018-08-31")]
        
        print('-' * 100)
        print("Training data shape:", train_data.shape)
        print("Testing data shape:", test_data.shape)
        print('-' * 100)
        
        # save data
        train_data.to_csv('Data/train_data.csv', index=False)
        test_data.to_csv('Data/test_data.csv', index=False)
        
        return train_data, test_data

