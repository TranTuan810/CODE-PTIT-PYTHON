

def sum(n):
    res = 0
    while(n > 0):
        res += n%10
        n//=10
    return res%10 == 0    

def check(n):
    s = str(n)
    a = [int(i) for i in s]
    for i in range(0, len(a)-1):
        if(abs(a[i] - a[i+1]) != 2): return False

    return True

t = int(input())
while(t > 0):
    n = int(input())
    func = lambda x: "YES" if(sum(x) and check(x)) else "NO"
    print(func(n))
    t-=1
