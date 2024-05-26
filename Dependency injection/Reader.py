from CsvConverter import CsvConverter
import linecache
import time

class Reader:
    def __init__(self, file_path="dSST.csv", stride=5):
        self.file_path = file_path
        self.stride = stride
        self.current_line = 2
        self.header = linecache.getline(self.file_path, 1)
        self.converter = CsvConverter(self.header, "")

    def __iter__(self):
        return self

    def __next__(self):
        lines = []
        for i in range(self.stride):
            line = linecache.getline(self.file_path, self.current_line)
            if not line:
                if lines:
                    return lines
                else:
                    raise StopIteration

            self.converter.values = line
            lines.append(self.converter.csv_to_json())
            self.current_line += 1

        time.sleep(5)
        return lines