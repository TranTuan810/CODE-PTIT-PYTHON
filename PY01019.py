

from math import *

def check(a, b):
    for i in range(1, len(a)):
        if(abs(ord(a[i]) - ord(a[i-1])) != abs(ord(b[i]) - ord(b[i-1]))):
            return False

    return True

if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        s = input().split()
        a = list(s[0])
        b = a[::-1]
        if(check(a, b)): print("YES")
        else: print("NO")

        t -= 1