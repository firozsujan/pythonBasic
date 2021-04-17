# Task # HackerRank # String validator
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False 
    
    for i in s:
        if i.isalnum():
            isalnum = True
            break
    
    for i in s:
        if i.isalpha():
            isalpha = True
            break
    
    for i in s:
        if i.isdigit():
            isdigit = True
            break
    
    for i in s:
        if i.islower():
            islower = True
            break
    
    for i in s:
        if i.isupper():
            isupper = True
            break
        
    print(isalnum)    
    print(isalpha)    
    print(isdigit)    
    print(islower)    
    print(isupper)
