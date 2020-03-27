import math
def square(n):
    for i in range (1,math.sqrt(n):
        if (i*i==n):
            return 1
    return 0
a = int(input())
b = int(input())

for i in range(a-1,b+1):
    if (square(i)==1):
        print(i)
    