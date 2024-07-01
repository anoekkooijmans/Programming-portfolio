import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
        
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
        
    def process_data(self, df):
        # drop low quality columns
        df = df.copy()
        df.drop(['sensor_15', 'sensor_50'],inplace = True,axis=1)
        
        #set timestamp to data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('timestamp')
        
        X = self.handle_missing_values(df)
        X = self.scale_data(X)
        
        return X
    

        
