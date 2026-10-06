
from math import *

s = input()
n, k = map(int, s.split())
a = [i for i in range(1, int(pow(10, k)))]
b = list(filter(lambda x: gcd(x, n) == 1 and str(x).__len__() == k, a))
func = lambda x: [print(x[i], end = " ") for i in range(0, min(len(b), 10))]
while(len(b) != 0):
    func(b)
    b[0:10] = []
    print()