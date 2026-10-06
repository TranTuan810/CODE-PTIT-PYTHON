
from math import *


def taget(n):
    cnt = 0
    for i in range(1, n):
        if(gcd(n, i) == 1): cnt+=1
    return cnt

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n%i == 0): return False
    return n > 1

def check(n):
    return snt(taget(n)) 

if __name__ == '__main__':
    t = int(input())
    while(t >0):
        n = int(input())
        if(check(n)): print("YES")
        else: print("NO")
        t -= 1