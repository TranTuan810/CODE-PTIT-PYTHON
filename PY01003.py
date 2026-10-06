

import math
def bienDoi(n):
    cnt = 0
    nho = 0
    while(n > 10):
        d = n%10
        if(d + nho >= 5): nho = 1
        else: nho = 0
        cnt += 1
        n//=10
    print((n + nho) * pow(10, cnt))

        


if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        bienDoi(n)
        t-=1
