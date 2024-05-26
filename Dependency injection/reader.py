import linecache
import time
import json

class CsvConverter:
    
    def __init__(self, header, values):
        self.header = header
        self.values = values
    
    def csv_to_json(self):
        
        keys = self.header.strip("\n").split(",")
        vals = self.values.strip("\n").split(",")
        
        json_dict = dict(zip(keys,vals))
        json_string = json.dumps(json_dict)

        return json_string

class Reader:
    
    def __init__(self, file_path = "dSST.csv", stride=5):
        self.file_path = file_path
        self.stride = stride
        self.current_line = 2
        self.header = linecache.getline(self.file_path, 1)
        self.converter = CsvConverter(self.header,"")
        
    def __iter__(self):
        return self
    
    def __next__(self):
        lines = []
        for i in range(self.stride):
            line = linecache.getline(self.file_path, self.current_line)
            if not line:
                if lines:  # If there are lines collected, return them before stopping iteration
                    return lines
                else:  # If no lines are collected, stop iteration
                    raise StopIteration

            self.converter.values = line
            lines.append(self.converter.csv_to_json())
            self.current_line += 1

        time.sleep(5) 
        return lines
    
# Add functionality to the Reader-class, so that the code below will work.
if __name__=='__main__':
    r = Reader('dSST.csv', 5)
    for i in r:
        print (len(i))