# Task # HackerRank # SwapCase

# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    newString = ''
    for i in s:
        if i.isupper():
            newString = newString + i.lower()
        else: 
            newString = newString + i.upper()
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
