import csv

customers = open('customers.csv', 'r')

outfile = open('customers_country.csv', 'w')
outfile.write('Full name, Country\n')

csv_file = csv.reader(customers)

#to skip the header
next(csv_file)

cust_num = 0
for rec in csv_file:
    cust_num += 1
    outfile.write(f'{rec[1]} {rec[2]}, {rec[4]}\n')
    
outfile.write(f'Total number of customers {cust_num}')

customers.close()
outfile.close()
