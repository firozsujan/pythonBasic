# Task # HackerRank # Text Wrap

# https://www.hackerrank.com/challenges/text-wrap/problem



import textwrap

def wrap(string, max_width):
    j=0
    newString = ""
    for i in string:
        newString =newString+i
        j += 1
        if j==max_width:
           newString = newString + '\n'
           j=0
    return newString
  
# another way using textwrap
def wrap2(string, max_width):
   return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
