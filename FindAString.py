# Task # hackerRank # Find a String
# https://www.hackerrank.com/challenges/find-a-string/problem



def count_substring(string, sub_string):
    lenOfSubString = len(sub_string)
    count = 0
    for i in range(len(string)):
        if sub_string == string[i: i+lenOfSubString]:
            count +=1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
