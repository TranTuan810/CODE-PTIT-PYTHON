
from math import *

def phanTich(n):
    print(1, end = "")
    if(n != 1): print(" * ", end = "")
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            cnt = 0
            while(n%i == 0):
                n/=i
                cnt += 1
            if(n == 1):print("{}^{}".format(i, cnt), end = "")
            else: print("{}^{} * ".format(i, cnt), end = "")
    if(n > 1):print("{}^{}".format(int(n), 1), end = "")
    print()

t = int(input())
while(t > 0):

    n = int(input())
    phanTich(n)
    t-= 1