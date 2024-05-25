import json

class CsvConverter:
    
    def __init__(self, header, values):
        self.header = header
        self.values = values
        
        
    def csv_to_json(self):
        
        keys = self.header
        vals = self.values
        
        json_dict = dict(zip(keys.split(','), vals.split(',')))
        json_string = json.dumps(json_dict)

        return json_string
    

                        
                
                