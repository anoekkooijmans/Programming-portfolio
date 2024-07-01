import pandas as pd 
from sklearn.ensemble import IsolationForest
import joblib
import json
from DataPreprocessor import DataPreprocessor

class TrainModel:
    """Trains model using the provided dataset"""
    def __init__(self, config="application.json"):
        # Load config
        with open(config) as f:
            config = json.load(f)
        self.output_dir = config["output_directory"]
    
    def predict(self, df, X, config="application.json"):
        df = df.copy()
        normal_rows = df[df['machine_status'] == 'NORMAL']
        outliers_fraction = 1 - (len(normal_rows) / len(df))
        
        algorithm = IsolationForest(contamination=outliers_fraction, n_jobs = -1)
        y_pred = algorithm.fit(X).predict(X)
        
        print('-' * 100)
        print("Isolation Forest")
        print("Number of anomolies detected:")
        print(pd.Series(y_pred).value_counts())
        print('-' * 100)        
        
        # Save trained model
        joblib.dump(algorithm, f'{self.output_dir}/isolation_forest_model.joblib')
        
        df["Isolation Forest"] = y_pred
        
        return df
        

    
        
    
        
