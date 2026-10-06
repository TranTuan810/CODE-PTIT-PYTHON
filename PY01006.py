


def check(n):
    cnt = 0
    while(n > 0):
        d = n % 10
        if(d != 4 and d != 7): return False
        n//=10
    return True

if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        if(check(n)): print("YES")
        else: print("NO")
        t -= 1