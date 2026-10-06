



def res(a, b, c):
    cnt = 0
    while(a <= c):
        a += a* (b/100)
        cnt += 1
    return cnt

if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        s = input()
        a, b, c = map(float, s.split())
        print(res(a, b, c))
        t -= 1