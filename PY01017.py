


if(__name__) == "__main__":
    t = int(input())
    while(t > 0):
        s = input()
        index = 0
        cnt = 0
        for i in range(0, len(s)):
            if(s[i] == s[index]): cnt += 1
            else:
                print(cnt, s[index], sep = "", end = "")
                index = i
                cnt = 1

        print(cnt, s[index],sep = "")
        t -= 1