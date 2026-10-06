
from math import *

s = input()
l, r = map(int, s.split())
for i in range (l, r):
    for j in range (i + 1, r):
        for k in range (j + 1, r + 1):
            # print(i, j, k)
            if(gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(k, i) == 1):
                print("({}, {}, {})".format(i, j, k))