def proceessStatement(insertStatement):
    
    if insertStatement[0] == 'insert': insert(insertStatement)
    elif 'print': printList(insertStatement)
    elif 'remove': remove(insertStatement)
    elif 'append': append(insertStatement)
    elif 'sort': sort(insertStatement)
    elif 'pop': pop(insertStatement)

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        
        insertStatement = []
        insertStatement = input().split(' ')
        proceessStatement(insertStatement)
    
    
    updatedList = []
        
        
def insert():
        position = int(insertStatement[1])
        insert = int(insertStatement[2])
        updatedList = list[:position] + [insert] + list[position:]
        # return updatedList
 
def printList(insertStatement):
        print(updatedList)
 
def remove(insertStatement):
    updatedList.remove(insertStatement[1])
    # return updatedList
 
def append(insertStatement):
    updatedList.append(insertStatement[1])
 
def sort(insertStatement):
    updatedList.sort
 
def pop(insertStatement):
    updatedList.pop()
 
    
    # print(list2)
