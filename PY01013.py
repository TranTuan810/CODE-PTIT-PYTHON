



from math import *

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0): return 0
    return n > 1

def sum(i):
    res = 0
    while(i > 0):
        res += i%10
        i//=10
    return res

if(__name__) == "__main__":
    t = int(input())
    while(t > 0):
        s = input()
        a, b = map(int, s.split())
        tmp = gcd(a, b)
        tmp = sum(tmp)
        if(snt(tmp)): print("YES")
        else: print("NO")
        t-= 1