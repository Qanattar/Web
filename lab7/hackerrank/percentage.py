def check(x,student):
    sum=0
    marks = x.split(' ')
    if (marks[0]==student):
        sum=int(marks[1])+int(marks[2])+int(marks[3])
    return sum/3
students  = []
N = int(input())
for i in range (1,N+1):
    s = input()
    students.append(s)
student = input()
for x in students:
    if (check(x,student)!=0):
        print(check(x,student))