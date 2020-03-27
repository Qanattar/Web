n = int(input())
arr = map(int, input().split())
my_list = sorted(list(set(arr)))
print (my_list[-2])
