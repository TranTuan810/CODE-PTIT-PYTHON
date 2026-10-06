from math import *

def biendoi(s, b):
    n = int(log2(b))
    s = s[::-1]
    tmp = ""
    i = 0
    while(i < len(s)):
        cur = 0
        for j in range(0, n):
            if(i + j > len(s) - 1): break
            cur = cur + int(s[i + j]) * int(pow(2, j))
        if(cur >= 10): tmp += chr(ord('A') + (cur - 10)) 
        else: tmp += str(cur)
        i += n
    tmp = tmp[::-1]
    return tmp

if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        b = int(input())
        s = input()
        if(b == 2):
            print(s)
        else:
            print(biendoi(s, b))
        t-=1