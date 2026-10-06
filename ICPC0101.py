





if(__name__) == '__main__':
    n = int(input())
    s = input()
    a = list(map(int, s.split()))
    b = []
    for i in range(len(a)):
        while(len(b) >= 2 and (b[-1] + b[-2]) % 2 == 0):
            del b[-1]
            del b[-1]

        b.append(a[i])
    while(len(b) >= 2 and (b[-1] + b[-2]) % 2 == 0):
         del b[-1]
         del b[-1]    

    print(len(b))

