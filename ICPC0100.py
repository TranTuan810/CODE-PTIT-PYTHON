

def check(a, m, n):
    b = a.copy()
    # print(a)
    # print(b)
    for i in range(n + m):
        # print(i)
        while(max(b[i], b[i+1]) > 2*min(b[i], b[i+1])):    
            b.insert(i + 1, (max(b[i], b[i+1]) + 2 - 1)//2)
        # print(b)
        if(i == len(b) - 2): break

    # print(b)
    for i in range(len(b)-1):
        if(max(b[i], b[i+1]) > 2* min(b[i], b[i+1])):
            return False
    return m >= len(b) - n

if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        s = input()
        a = list(map(int, s.split()))
        l = 0
        r = 1000
        res = 1000
        while(l <= r):
            m = (l + r)//2
            if(check(a, m, n)):
                # print(m)
                res = min(res, m)
                r = m-1
            else: l = m + 1

        print(res)
        # print(len(a) - n)
        t-= 1