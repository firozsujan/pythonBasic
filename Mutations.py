# Task # hackerRank # Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    newString = ""
    l = list(string)
    l[position] = character
    newString = ''.join(l)
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
