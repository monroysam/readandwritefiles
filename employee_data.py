def main():

    import csv
    
    infile = open('employee_data.csv', 'r')

    for line in infile:
        print(line[1])
        print(line[2])
