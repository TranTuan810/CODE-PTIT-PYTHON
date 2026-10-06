


if(__name__) == "__main__":
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    cnt = [0]
    cnt = cnt * 256
    for i in range(len(string)):
        cnt[ord(string[i])] = i

    while(1):
        t = input().split()
        if(len(t) == 1): break

        k = int(t[0])
        s = list(t[1])
        b = []
        # for i in range(len(s)):
        #     b.append(string[(cnt[ord(s[i])] + k)%28])
        b = [string[(cnt[ord(i)] + k)%28] for i in s]
        b = b[::-1]
        for i in b: print(i, end ="")
        print()
