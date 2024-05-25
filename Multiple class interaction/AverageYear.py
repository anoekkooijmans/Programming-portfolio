from CsvConverter import CsvConverter
from Reader import Reader
import json
import pandas as pd
import matplotlib.pyplot as plt

class AverageYear:
        def __init__(self):
            self.reader = Reader()
            self.data = []
            self.average_df = []            
            
        def calculate_average(self):
            
            while True:
                lines = self.reader.get_lines()
                if not lines:
                    break
                
                for line in lines:
                    data_dict = json.loads(line)
                    self.data.append(data_dict)
                    
            df = pd.DataFrame(self.data)
            temp_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            df.index = df['Year']
            df = df[temp_cols].apply(pd.to_numeric)
            df["Average"] = df.mean(axis=1)
                        
            return df
        
        def create_plot(self):
            
            df = self.calculate_average()

            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df['Average'], color='b', linestyle='-')
            plt.xticks(rotation=90)
            plt.xticks(df.index[::5])
            plt.title('Average Temperature Anomaly Per Year')
            plt.xlabel('Year')
            plt.ylabel('Average Temperature Anomaly')

            return plt
