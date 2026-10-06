
def palindrome(a):
    if(len(a) < 2): return 0
    else:
        l = 0
        r = len(a) - 1
        while(l <= r):
            if(a[l] != a[r]): return 0
            l += 1
            r -= 1
        return 1



def check(s):
    a = list(s)
    return palindrome(a)


for __ in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    s = str(sum)
    func = lambda x: "YES" if(check(s)) else "NO"
    print(func(s))
