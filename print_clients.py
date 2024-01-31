def main():
    infile = open('clients.txt', 'r')

    it_num = 0
    for x in infile:
        it_num += 1
        print(f'{it_num}. {x}', end = '')

    print()    
    print(f'Total number of clients: {it_num}')

    infile.close()

main()