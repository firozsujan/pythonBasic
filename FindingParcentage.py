# Task # HackerRank # finding parcentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    averageMarks = 0
    sum = 0
    for key, value in student_marks.items():
        
        if key == query_name:
            for j in value:
                sum = sum + j
            averageMarks = sum/len(value)
    
    print("%.2f" % averageMarks)
