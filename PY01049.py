
from math import *

def nt(x):
    for i in range(2, int(sqrt(x))):
        if(x % i == 0): return False
    return x > 1


for __ in range(int(input())):
    s = input()
    a = [i for i in list(s) if(i == '2' or i == '3' or i == '5' or i == '7')]
    func = lambda x: "YES" if(nt(x) and len(a) > (len(list(s)) - len(a))) else "NO"
    print(func(len(list(s))))