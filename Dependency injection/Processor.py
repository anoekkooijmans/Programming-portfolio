from Reader import Reader
from AverageYear import AverageYear
from AverageMonth import AverageMonth

class Processor:
    def __init__(self):
        self.reader = Reader()
        self.average_year = AverageYear()
        self.average_month = AverageMonth()
    
    def display_menu(self):
        print("********************")
        print("Welcome to the awesome data processor.")
        print("********************")
        print("Please select one of the following:")
        print("  1. get horizontal data")
        print("  2. get vertical data")
        print("  3. get next stride of data")
        print("  9. quit and exit")

    def process(self):
        while True:
            self.display_menu()
            selection = input("Please enter your selection: ")
            if selection == '1':
                self.process_horizontal_data()
            elif selection == '2':
                self.process_vertical_data()
            elif selection == '3':
                self.process_next_stride()
            elif selection == '9':
                print("bye!")
                break
            else:
                print("Invalid selection, please try again.")

    def process_horizontal_data(self):
        avg_year_df = self.average_year.calculate_average()
        print("horizontal data goes here")
        print(avg_year_df.mean(axis=0).to_dict())

    def process_vertical_data(self):
        avg_month_series = self.average_month.calculate_average()
        print("vertical data goes here")
        print(avg_month_series.to_dict())

    def process_next_stride(self):
        try:
            next_data = next(self.reader)
            self.average_year.update(next_data)
            self.average_month.update(next_data)
            print("Next stride of data processed.")
        except StopIteration:
            print("No more data available.")