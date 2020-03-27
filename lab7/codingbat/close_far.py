def diff(a,b):
    if (a-b<=1 or a-b>=-1):
        return 1
    if (a-b>=2 or b-a>=2):
        return 2


def close_far(a,b,c):
    if (diff(a,b)==1 and diff(a,c)==2 and diff(b,c)==2):
        return true
    if (diff(a,c)==1 and diff(a,b)==2 and diff(b,c)==2):
        return true

