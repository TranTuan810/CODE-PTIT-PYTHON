
from math import *

def check(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0): return 0
    return n > 1

for __ in range(int(input())):
    s = input()
    sum = 0
    for x in s:
        sum += ord(x) - ord('0')
    func = lambda x: "YES" if(check(x)) else "NO" 
    print(func(sum))