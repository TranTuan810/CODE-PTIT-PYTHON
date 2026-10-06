
def check(n):
    a = list(str(n))
    for i in a:
        if(int(i)%2 != 0): return False 
    return True
def biendoi(x):
    c = x + x[::-1]
    sum = 0
    for i in c:
        sum = sum* 10 + (ord(i) - ord('0'))
    return sum

t = int(input())
while(t > 0):
    s = input()
    tg = 0
    n = len(s)//2
    for i in range(0, n):
        tg = tg * 10 + (ord(s[i]) - ord('0'))
    if(len(s) %2 != 0): tg = tg* 10 + (ord(s[len(s)//2]) - ord('0'))
    a = [i for i in range(2, tg + 1) if check(i)]
    func = lambda x: biendoi(x)
    b = [func(list(str(i))) for i in a]
    func2 = lambda x: [print(i, end = " ") for i in b if i <int(s)]
    func2(b)
    print()
    t-=1