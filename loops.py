# Task # HackerRank #loops
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .



if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
        
# Task # HackerRank # Write a function to find out leap year

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0 :
        leap = True
    elif year % 400 == 0 :
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
