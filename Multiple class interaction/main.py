from CsvConverter import CsvConverter
from Reader import Reader
from AverageYear import AverageYear
from AverageMonth import AverageMonth

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
    
def step_2a():
    average = AverageYear()
    plt = average.create_plot()
    plt.show()
    plt.close()
    
def step_2b():
    average = AverageMonth()
    plt = average.create_plot()
    plt.show()
    plt.close()

    
if __name__ == "__main__":
    step_2b()

