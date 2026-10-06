



t = int(input())
test = 1
while(t > 0):
    s1 = input()
    s2 = input()
    a = list(s1)
    b = list(s2)

    a.sort()
    b.sort()
    if(a == b): print("Test {}:".format(test), "YES")
    else: print("Test {}:".format(test), "NO")

    t-=1
    test += 1