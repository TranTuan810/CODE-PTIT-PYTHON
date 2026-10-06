


def check(n):
    cnt = 0
    while(n > 0):
        d = n % 10
        if(d == 4 or d == 7): cnt += 1
        n//=10
    return cnt == 4 or cnt == 7

if __name__ == '__main__':
    n = int(input())
    if(check(n)): print("YES")
    else: print("NO")