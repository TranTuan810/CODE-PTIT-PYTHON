


def check(x):
    if(len(x) < 3): return False
    p = -1
    for i in range(len(x) - 1):
        if(x[i] < x[i + 1]): continue
        elif(x[i] == x[i + 1]): return False
        else: 
            p = i
            break
    # print(p)
    for i in range(p, len(x)-1):
        if(x[i] <= x[i + 1]): return False
    return True

t = int(input())
while(t > 0):
    s = input()
    a = list(s)
    func = lambda x: "YES" if check(x) else "NO"
    print(func(a))
    t -=1