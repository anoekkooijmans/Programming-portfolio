from CsvConverter import CsvConverter
from Reader import Reader
import json
import pandas as pd
import matplotlib.pyplot as plt

class AverageMonth:
        def __init__(self):
            self.data = []
            
        def update(self,data):
            self.data.extend(data)
            self.create_plot()
            
        def calculate_average(self):
            
            lines = self.data
            
            dict_list = []    
            for line in lines:
                data_dict = json.loads(line)
                dict_list.append(data_dict)
                    
            df = pd.DataFrame(dict_list)
            temp_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            df.index = df['Year']
            df = df[temp_cols].apply(pd.to_numeric)
            average_per_month = df.mean()
                        
            return average_per_month
        
        def create_plot(self):
            
            df = self.calculate_average()

            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df.values, marker='o', linestyle='-')
            plt.xlabel('Month')
            plt.ylabel('Average Temperature Anomaly')
            plt.title('Average Temperature Anomaly per Month')
            plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
            plt.tight_layout()
            
            plt.show()
            plt.close()
        
            return plt