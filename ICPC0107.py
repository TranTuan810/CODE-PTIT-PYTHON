

def Sum(a, b):
    X1 = a.copy()
    X2 = b.copy()
    X1.reverse()
    X2.reverse()
    for i in range(len(X2), len(X1)):
        X2.append('0')
    nho = 0
    res = ""
    for i in range(0, len(X1)):
        c_res = ord(X1[i]) - 2*ord('0') + ord(X2[i]) + nho
        nho = c_res//10
        res += chr(ord('0') + c_res%10)
    if(nho == 1): res += '1'
    res = res[::-1]
    return res



def  sumMax(X1, X2, p, q):
    for i in range(len(X1)):
        if(int(X1[i]) == p): X1[i] = chr(q + ord('0'))
    for i in range(len(X2)):
        if(int(X2[i]) == p): X2[i] = chr(q + ord('0'))
    if(len(X1) >= len(X2)): return Sum(X1, X2)
    else: return Sum(X2, X1)

def sumMin(X1, X2, p, q):
    for i in range(len(X1)):
        if(int(X1[i]) == q): X1[i] = chr(p + ord('0'))
    for i in range(len(X2)):
        if(int(X2[i]) == q): X2[i] = chr(p + ord('0'))
    if(len(X1) >= len(X2)): return Sum(X1, X2)
    else: return Sum(X2, X1)

if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        s = input()
        a, b = map(int, s.split())
        q = min(a, b)
        p = max(a, b)
        s1 = input().split()
        X1 = []
        X2 = []
        if(len(s1) > 1): 
            X1 = list(s1[0])
            X2 = list(s1[1])
        else:
            X1 = list(s1[0])
            s2 = input()
            X2 = list(s2)

        # print(X1, X2)    
        print(sumMin(X1, X2, q, p), sumMax(X1, X2, q, p))
        t-=1
