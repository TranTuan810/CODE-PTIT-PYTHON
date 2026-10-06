
global n
b = []

def check():
    tmp =['A', 'B', 'C'] 
    mp = {}
    mp = mp.fromkeys(tmp, 0)
    for i in b:
        mp[i] += 1
    return mp['A'] <= mp['B'] and mp['B'] <= mp['C'] and mp['A'] != 0 and mp['B'] != 0 and mp['C'] != 0


def ql(i):
    if(i > n):
        if(check()):
           print(*b, sep = "")
        return
    for j in range(ord('A'), ord('D')):
        b.append(chr(j))
        ql(i + 1)
        b.pop()
        
for i in range(3, int(input()) + 1):
    n = i
    ql(1)

# def Try(s, l, a, b, c):
#     if a <= b and b <= c and a > 0 and len(s) == l:
#         print(s)
#     if len(s) < l:
#         Try(s + "A", l, a + 1, b, c)
#         Try(s + "B", l, a, b + 1, c)
#         Try(s + "C", l, a, b, c + 1)

# n = int(input())
# for i in range(3, n + 1):
#     Try("", i, 0, 0, 0)