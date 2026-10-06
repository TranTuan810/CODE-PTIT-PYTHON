

# def biendoi(n, k):
#     a = []
#     while(n > 0):
#         a.append(n%k)
#         n//= k
#     return a[::-1]
# def change(i):
#     if(i <= 9): return i
#     else:
#         return chr(ord('A') + i -10)

# t = int(input())
# while(t > 0):
#     s = input()
#     n, k = map(int, s.split())
#     b = [change(i) for i in biendoi(n, k)]
#     print(*b, sep="")
#     # print()
#     t -=1

a, b, m = map(int, input().split())
if m>3:
    cnt = 0
    for i in [0,1]:
        if a<=i and i<=b: cnt+=1
    print(cnt)
elif m==3:
    cnt = 0
    for i in [0, 1, 6643, 1422773, 5415589]:
        if a<=i and i<=b: cnt+=1
    print(cnt)
elif m==2:
    cnt = 0
    for i in range(1,10000):
        s1 = bin(i)[2:]
        s2 = ''.join(reversed(s1))  
        arr = [s1+s2, s1+'0'+s2, s1+'1'+s2]
        for j in arr:
            x = int(j,2)
            if a<=x and x<=b: cnt+=1
    for i in [0,1]:
        if a<=i and i<=b: cnt+=1
    print(cnt)
else: print(0)