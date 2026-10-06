
from math import *

t = int(input())
while(t > 0):
    n = input().strip()
    func = lambda x: "YES" if gcd(int(x), int(x[::-1])) ==1 else "NO"
    print(func(n))
    t -= 1

