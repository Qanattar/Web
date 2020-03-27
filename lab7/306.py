def min(a,b,c,d):
    my_list = [a,b,c,d]
    my_list.sort()
    return my_list[0]
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a,b,c,d))