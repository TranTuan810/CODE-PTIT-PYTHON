from math import *

def nt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0): return False
    return n > 1
def check(a):
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
        if((int(a[i]) + i) % 2 != 0): return False
    return nt(sum)

for __ in range(int(input())):
    s = input()
    a = list(s)
    # print(*a)
    func = lambda x: "YES" if check(x) else "NO"
    print(func(a))