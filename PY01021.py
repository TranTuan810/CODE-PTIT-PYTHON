






if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        s = input()
        a = list(s)
        b = [i for i in a if i.isalpha()]
        c = [i for i in a if i.isdigit()]
        b.sort()
        for i in b: print(i, end = "")
        sum = 0
        for i in c: sum += int(i)
        print(sum)
        t-=1
