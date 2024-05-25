from CsvConverter import CsvConverter
import json

def step_1():
    keys = 'a,b,c,d'
    vals = '3,2,1,5'
    line = CsvConverter(header = keys, values = vals)
    json_line = line.csv_to_json()
    print(json_line)
        
if __name__ == "__main__":
    step_1()

        