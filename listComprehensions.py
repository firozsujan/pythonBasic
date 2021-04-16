# Task # HackerRank # ListComprehensions

# https://www.hackerrank.com/challenges/list-comprehensions/problem

def prepareList(x, y, z, n):
        
        finalList =[]
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    list = []
                    sum = i+j+k
                    if sum != n:
                            list.append(i)
                            list.append(j)
                            list.append(k)
                            finalList.append(list)
        
        return finalList


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list = prepareList(x, y, z, n)
    print(list)
    
