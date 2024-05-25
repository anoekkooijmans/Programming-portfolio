from CsvConverter import CsvConverter
from Reader import Reader

def step_1a():
    keys = 'a,b,c,d'
    vals = '3,2,1,5'
    line = CsvConverter(header = keys, values = vals)
    json_line = line.csv_to_json()
    print(json_line)
    
def step_1b():
    reader = Reader('dSST.csv')
    print(reader.get_lines())  # Returns lines 2-6 as JSON
    print(reader.get_lines())  # Returns lines 7-11 as JSON
    print(reader.get_lines())
        
if __name__ == "__main__":
    step_1b()

