# Task 9 # HakarRank # Lists

# https://www.hackerrank.com/challenges/python-lists/problem



def proceessStatement(insertStatement, list):
    if insertStatement[0] == 'insert': return insert(insertStatement, list)
    elif insertStatement[0] == 'print': return printList(insertStatement, list)
    elif insertStatement[0] == 'remove': return remove(insertStatement, list)
    elif insertStatement[0] == 'append': return append(insertStatement, list)
    elif insertStatement[0] == 'sort': return sort(insertStatement, list)
    elif insertStatement[0] == 'pop': return pop(insertStatement, list) 
    elif insertStatement[0] == 'reverse': return reverse(insertStatement, list)    
        
def insert(insertStatement, list):
        position = int(insertStatement[1])
        insert = int(insertStatement[2])
        updatedList = []
        updatedList = list[:position] + [insert] + list[position:]
        return updatedList
 
def printList(insertStatement, list):
        print(list)
        return list
 
def remove(insertStatement, list):
    list.remove(int(insertStatement[1]))
    return list
 
def append(insertStatement, list):
    list.append(int(insertStatement[1]))
    return list
 
def sort(insertStatement, list):
    list.sort()
    return list
 
def pop(insertStatement, list):
    list.pop()
    return list
 
def reverse(insertStatement, list):
    list.reverse()
    return list

if __name__ == '__main__':
    N = int(input())
    list = []
    
    for i in range(N):
        insertStatement = []
        insertStatement = input().split(' ')
        list = proceessStatement(insertStatement, list)
    
