import json 
import linecache
from tkinter import W

class CsvToJson:

    def __init__(self, headers):
        self.headers = headers.strip().split(',')

    def csv_to_json(self, csv_rows):
        json_val = []
        for row in csv_rows:
            row = row.split(',')
            assert len(row) == len(self.headers), 'Length of data and headers should be the same'
            json_val.append(dict(zip(self.headers, [float(x) for x in row])))
        return json.dumps(json_val)

class Reader:
    def __init__(self, filename, stride_length):
        self.filename = filename
        self.stride_length = stride_length
        self.converter = CsvToJson(linecache.getline(self.filename, 1))

    def __iter__(self):
        return self

    def __next__(self):
        lines = []
        with open(self.filename, 'r') as file:
            for _ in range(self.stride_length):
                line = file.readline().strip()
                if not line:
                    break
                lines.append(line)
        if not lines:
            raise StopIteration
        return self.converter.csv_to_json(lines)
    
# Add functionality to the Reader-class, so that the code below will work.
if __name__=='__main__':
    r = Reader('dSST.csv', 5)
    for i in r:
        print (len(i))