# Task 10 # HackerRank
# https://www.hackerrank.com/challenges/python-tuples/problem


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

