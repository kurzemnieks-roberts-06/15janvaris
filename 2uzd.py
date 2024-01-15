import csv


def print_second_column_data(file_path):
  
    with open(file_path, 'r') as file:
        
        csv_reader = csv.reader(file)

  
        for row in csv_reader:
           
            print(row[1])


file_path = input('Enter the path of the CSV file: ')


print_second_column_data(file_path)
