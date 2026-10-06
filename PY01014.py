


if(__name__) == "__main__":
    s = input()
    a, k, n = map(int, s.split())
    r = 0
    if(a%k != 0): r = k - a%k
    ok = 0
    for i in range(0, n -a +1):
        if(i*k + r > n - a): break
        if(i*k + r != 0):
            print(i*k + r, end = " ")
            ok = 1

    if(ok == 0): print("-1")

