
from math import *

def sum(a):
    if(a[0] == 0): return -1
    dg = 0
    for i in a:
        dg = dg*10 + i
    return dg

def sinh(a):
    n = len(a)
    i = len(a)-2
    while(i >= 0 and a[i] <= a[i+1]):
        i-=1
    # print(i)
    if(i == -1):
        return -1
    else:
        j = n-1
        while(a[j] >= a[i] or a[j] == a[j-1]):
            j -=1

        a[i], a[j] = a[j], a[i]

        return sum(a)



t = int(input())
while(t > 0):
    s = input().strip()
    a = list(map(int, s))
    i = 0
    if(len(a) == 1): print(*a)
    else: 
        while(a[i] == 0):
            a[i:i+1] = []
            i+=1
        print(sinh(a))
    t-=1