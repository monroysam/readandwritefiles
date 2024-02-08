print()

def main():

    #get csv data
    import csv
    infile = open('employee_data.csv', 'r')
    emp_data = csv.reader(infile)
    next(emp_data)

    #create lists for organization
    efficient_list = []
    inefficient_list = []
    emp_40s = []
    emp_30s = []
    emp_20s = []

    #run loop and convert data
    for line in emp_data:
        name = line[1]
        hours_worked = float(line[4])
        productivity = float(line[5])
        efficiency = productivity / hours_worked
        age = float(line[2])

        #calculations
        if efficiency > 2:
            efficient_list.append(name)
        elif efficiency < 1:
            inefficient_list.append(name)
        
        if age < 30:
            emp_20s.append(name)
        elif age < 40:
            emp_30s.append(name)
        else:
            emp_40s.append(name)

    #print high efficiency 
    print('Highly Efficiency Individuals')
    for name in efficient_list:
        print(name)

    #print low efficiency
    print()
    print('Low Efficiency Individuals')
    for name in inefficient_list:
        print(name)

    #print employyes in 40s
    print()
    print('Employees in their 40s')
    for name in emp_40s:
        print(name)
    print()
    print(f'Total number of employees in their 40s: {len(emp_40s)}')

    #print employyes in 30s
    print()
    print('Employees in their 30s')
    for name in emp_30s:
        print(name)
    print()
    print(f'Total number of employees in their 30s: {len(emp_30s)}')

    #print employyes in 20s
    print()
    print('Employees in their 20s')
    for name in emp_20s:
        print(name)
    print()
    print(f'Total number of employees in their 20s: {len(emp_20s)}')
    print()

#call the function
main()
