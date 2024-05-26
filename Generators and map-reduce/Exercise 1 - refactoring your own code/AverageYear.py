from CsvConverter import CsvConverter
from Reader import Reader
import json
import pandas as pd
import matplotlib.pyplot as plt

class AverageYear:
        def __init__(self):         
            self.data =[]
            
        def update(self,data):
            self.data.extend(data)
            self.create_plot()
            
        def calculate_average(self):
            
            lines = self.data

            dict_list = [json.loads(line) for line in self.data]
            df = pd.DataFrame(dict_list)
            temp_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            df.index = df['Year']
            df = df[temp_cols].apply(pd.to_numeric)
            df["Average"] = df.mean(axis=1)
                        
            return df
        
        def create_plot(self):
            
            df = self.calculate_average()

            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df['Average'], marker='o', color='b', linestyle='-')
            plt.xticks(rotation=90)
            plt.title('Average Temperature Anomaly Per Year')
            plt.xlabel('Year')
            plt.ylabel('Average Temperature Anomaly')
            plt.show()
            plt.close()
            
            return plt
