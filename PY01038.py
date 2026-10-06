

def res(a):
    t = 1000
    for i in range(t):
       b = a[::-1]
       str1 = "".join(a)
       str2 = "".join(b)
       cur = int(str1) + int(str2)
       if(cur% 7 == 0): return cur
       a = list(str(cur))
    return -1 

t = int(input())
while(t > 0):
    n = input()
    a = list(n)
    if(int(n) % 7 == 0): print(n)
    else: print(res(a))
    t-=1