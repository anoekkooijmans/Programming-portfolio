from CsvConverter import CsvConverter
import linecache
import time

class Reader:
    
    def __init__(self, file_path = "dSST.csv", stride=5):
        self.file_path = file_path
        self.stride = stride
        self.current_line = 2
        self.header = linecache.getline(self.file_path, 1)
        self.converter = CsvConverter(self.header,"")
        self.observers = set()
    
    def get_lines(self):
        
        lines = []
        for i in range(self.stride):
            line = linecache.getline(self.file_path, self.current_line)
            if not line:
                return ""

            self.converter.values = line
            lines.append(self.converter.csv_to_json())
            self.current_line += 1
                
        self.notify_observers(lines)
        time.sleep(5) 

        # return aan wie? het is juist onderdeel van het observer-pattern
        # dat er niks geretourneerd hoeft te worden.
        return lines 
    

    def add_observer(self,observer):
        self.observers.add(observer)
    
    def remove_observer(self):
        # dit werkt niet (vscode geeft er ook een compile-error op)
        # die `observer` is niet gedefinieerd; klopt ook, want welke
        # observer wil je dan uit die lijst halen?
        if observer in self.observers:
            self.observers.remove(observer)
        
    def notify_observers(self,data):
        for observer in self.observers:
            observer.update(data)
            
    
                
