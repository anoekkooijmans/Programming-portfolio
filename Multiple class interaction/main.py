from CsvConverter import CsvConverter
from Reader import Reader
from AverageYear import AverageYear
from AverageMonth import AverageMonth

def read_lines():
    prod = Reader('dSST.csv')
    cons1 = AverageYear()
    cons2 = AverageMonth()
    prod.add_observer(cons1)
    prod.add_observer(cons2)
    print(prod.get_lines())
    
if __name__ == "__main__":
    read_lines()
