




if(__name__) == "__main__":
    s = input()
    t = input()
    n = int(input())
    for i in range (0, len(s)):
        if(i == n -1): print(t,s[i], sep="", end="")
        else: print(s[i], end = "")
    if(n >= len(s) + 1): print(t)
    