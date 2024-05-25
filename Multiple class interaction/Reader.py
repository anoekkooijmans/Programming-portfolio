from CsvConverter import CsvConverter
import linecache

class Reader:
    
    def __init__(self, file_path = "dSST.csv", stride=5):
        self.file_path = file_path
        self.stride = stride
        self.current_line = 2
        self.header = linecache.getline(self.file_path, 1)
        self.converter = CsvConverter(self.header,"")
    
    def get_lines(self):
        lines = []
        # Only get given number of lines
        for i in range(self.stride):
            line = linecache.getline(self.file_path, self.current_line)
            # Return empty string if there are no more lines
            if not line:
                return ""

            # Convert to json
            self.converter.values = line
            lines.append(self.converter.csv_to_json())
            self.current_line += 1
                
        return lines
