

def check(s):
    a = int(s[0]) * 10 + int(s[1])
    b = int(s[len(s) - 2]) * 10 + int(s[len(s) - 1])
    return a == b

if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        s = input()
        if(check(s)): print("YES")
        else: print("NO")
        t-= 1

    
