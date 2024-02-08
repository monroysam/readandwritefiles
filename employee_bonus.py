def main():

    #get csv data
    import csv
    infile = open('employee_data.csv', 'r')
    emp_data = csv.reader(infile)
    next(emp_data)

    #print out data
    print()
    for line in emp_data:
        print()
        print()    
        salary = float(line[3])
        bonus_multiplier = float(line[7])
        bonus = bonus_multiplier * salary
        pay = salary + bonus
        print(f'Name: {line[1]}')
        print(f'Salary: $ {salary:10,.2f}')
        print(f'Bonus:  $ {bonus:10,.2f}')
        print(f'Pay:    $ {pay:10,.2f}')
    
#call function
main()