import json

class CsvConverter:
    
    def __init__(self, header, values):
        self.header = header
        self.values = values
    
    def csv_to_json(self):
        
        # dit had je ook in de constructor kunnen doen, aangezien
        # de headers / keys niet veranderen in de lifecycle van 
        # dit object.
        keys = self.header.strip("\n").split(",")

        vals = self.values.strip("\n").split(",")
        
        json_dict = dict(zip(keys,vals)) # spatie tussen de parameters
        json_string = json.dumps(json_dict)

        return json_string