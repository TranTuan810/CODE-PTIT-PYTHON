




t = int(input())
for __ in range(t):
    s = input()
    a = list(s)
    b = [i for i in a if(i == '1' or i == '2' or i == '0')]
    func = lambda b: "YES" if(len(a) == len(b)) else "NO"
    print(func(b))