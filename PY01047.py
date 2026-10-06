



from math import *

def nt(x):
    for i in range(2, int(sqrt(x) + 1)):
        if(x % i == 0): return False
    return x > 1


t = int(input())
for __ in range(t):
    s = input()
    a =list(s)
    a = a[-4::1]
    cur_str = "".join(a)
    b = int(cur_str)
    func = lambda x: "YES" if(nt(x)) else "NO"
    print(func(b))