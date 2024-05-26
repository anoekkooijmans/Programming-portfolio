import json

class CsvConverter:
    def __init__(self, header, values):
        self.header = header
        self.values = values

    def csv_to_json(self):
        keys = self.header.strip("\n").split(",")
        vals = self.values.strip("\n").split(",")
        json_dict = dict(zip(keys, vals))
        json_string = json.dumps(json_dict)
        return json_string