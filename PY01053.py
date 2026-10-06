
from math import *


for __ in range(int(input())):
    s = input()
    sum = 0
    for x in s:
        sum += ord(x) - ord('0')
    func = lambda x: "YES" if(x % 3 == 0) else "NO" 
    print(func(sum))