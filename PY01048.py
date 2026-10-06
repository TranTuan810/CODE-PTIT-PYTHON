
import sys


for __ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res = 0
    for i in range(2, 10**5):
        tmp = ((n * 2)//i - i + 1)//2
        if(i*(2*tmp + i -1)//2 == n and tmp > 0):
            # print(i, tmp)
            res += 1
    print(res)