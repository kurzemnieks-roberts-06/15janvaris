def print_file_content(file_path):

    with open(file_path, 'r') as file:
        
        lines = file.readlines()

       
        for line in lines:
     
            print(line.strip())


file_path = input('Enter the path of the text file: ')


print_file_content(file_path)