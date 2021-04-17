# Task # HackerRank # Designer door mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
   number = input().split(" ")
   N = int(number[0])
   M = int(number[1])
   #signs 
   a = '-'
   b = '.|.'
   c = 'WELCOME'
   
   # First half
   for i in range(1, N, 2):
        string = []
        for j in range(i):
            string.append(b)
        line = "".join(string)
        print(line.center(M, a))
   print(c.center(M, a))

   # Second half
   for i in range(N-2, 0, -2):
        string = []
        for j in range(i):
            string.append(b)
        line = "".join(string)
        print(line.center(M, a))
    
