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
        
        lines = [self._get_line() for _ in range(self.stride) if self._get_line()]
            if not line:
                return ""

            self.converter.values = line
            lines.append(self.converter.csv_to_json())
            self.current_line += 1
                
        self.notify_observers(lines)
        time.sleep(5) 

        return lines

    def add_observer(self,observer):
        self.observers.add(observer)
    
    def remove_observer(self):
        if observer in self.observers:
            self.observers.remove(observer)
        
    def notify_observers(self,data):
        for observer in self.observers:
            observer.update(data)
            
    
                
