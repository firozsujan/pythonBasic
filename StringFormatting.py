# Task # HackerRank # String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)[1:])
    printString = ''
    for i in range(1, number+1):
        for base in 'doXb':
            if base == 'd':
                width = len(bin(number)[2:])
            else :
                width = len(bin(number)[1:])
                
            printString = printString + "{:{width}{base}}".format(i, base=base, width=width)
        printString = printString + '\n'
        
    print(printString)
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
