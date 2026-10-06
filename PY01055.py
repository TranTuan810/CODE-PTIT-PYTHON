

def check(x):
    if(x.__len__() < 2): return 1
    else:
        if(x[0] == x[1]): return 0
        for i in range(0, x.__len__()):
            if(i % 2 == 0): 
                if(x[i] != x[0]): return 0
        return 1

for __ in range(int(input())):
    s = input()
    func = lambda x: "YES" if(x.__len__() % 2 != 0 and check(x)) else "NO"
    print(func(s))