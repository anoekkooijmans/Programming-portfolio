import pandas as pd

class DataPreprocessor:
    "Splits data into training and test sets"
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path).drop('Unnamed: 0', axis=1)

    def process_data(self):
        print("Pre-processing data")
        # Convert to datatime
        df = self.data
        
        # drop low quality columns
        df.drop(['sensor_15', 'sensor_50'],inplace = True,axis=1)
           
        return df
        
        
