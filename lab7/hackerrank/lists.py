my_list = []

def check(item):
    if item == 'print':
        print(my_list)
    elif item == 'sort':
        my_list.sort()
    elif item == 'pop':
        my_list.pop()
    elif item == 'reverse':
        my_list.reverse()
    elif item[0:6] == 'insert':
        inserts = item.split(' ')
        my_list.insert(int(inserts[1]), int(inserts[2]))
    elif item[0:6] == 'remove':
        inserts = item.split(' ')
        my_list.remove(int(inserts[1]))
    elif item[0:6] == 'append':
        inserts =item.split(' ')
        my_list.append(int(inserts[1]))
commands  = []
N = int(input())
for i in range (1,N+1):
    com =input()
    commands.append(com)
for x in commands:
    check(x)
