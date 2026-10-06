

def sum(t):
    res = 0
    for i in t:
        res += ord(i) - ord('0')
    return res


t = input()
a = [i for i in t]
if(len(a) == 1): print(1)
else:
    cnt = 0
    while(1):
        if(len(a) == 1):
           break
        # c_sum = sum(a, 0)
        a = [i for i in str(sum(a))]
        cnt += 1

    print(cnt)