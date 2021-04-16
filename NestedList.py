# Task # HackerRank # Nested List

# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([ name, score])
        
    list.sort(key=lambda x: x[1])
    minValue = list[0]
    for i in list:
        if i[1] != minValue[1]:
            secoundMinValue = i
            break
        
    sceoundMinValuSortedList = []
    
    for i in list:
        if i[1] == secoundMinValue[1]:
            sceoundMinValuSortedList.append(i[0])
        
    sceoundMinValuSortedList.sort()
    for i in sceoundMinValuSortedList:
        print(i)
