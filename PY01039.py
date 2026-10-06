
def check(x):
    for i in range(len(x)-2):
        if(x[i] != x[i+2]): return False
    return True


t = int(input())
while(t > 0):
    s = input()
    a = list(s)
    func = lambda x: "YES" if check(x) else "NO"
    print(func(a))
    t-=1