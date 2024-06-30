import pandas as pd
from sklearn.preprocessing import StandardScaler
from DataLoader import DataLoader

class DataPreprocessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data_loader = DataLoader(self.data_path)
        self.data = self.load_data()
        
    def load_data(self):
        data = pd.read_csv("Data/train_data.csv")
        return data

    def handle_missing_values(self,df):
        # Use mean of the column to handle missing values
        m, n = df.shape
        X = df.iloc[:,:n-1] # ignore machine status columns
        X = X.fillna(X.mean())
        return X
    
    def scale_data(self,X):
        scaler=StandardScaler()
        X_scaled = scaler.fit_transform(X)
        return X_scaled
        
    def process_data(self):
        print("\nPre-processing data")        
        # drop low quality columns
        df = self.data
        df.drop(['sensor_15', 'sensor_50'],inplace = True,axis=1)
        
        #set timestamp to data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')
        
        X = self.handle_missing_values(df)
        X = self.scale_data(X)
        
        return X
        
        
