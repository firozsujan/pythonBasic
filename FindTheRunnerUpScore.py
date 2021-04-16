# Task # HackerRank # Find the Runner-Up Score!

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    winner = arr[0]
    for i in arr:
        if i != winner:
            print(i)
            break
