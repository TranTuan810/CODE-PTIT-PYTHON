

def check(s):
    cnt = 0
    sz = len(s)
    for i in range(0, sz):
        if(s[i].islower()): cnt += 1
    if(cnt >= (sz - cnt)): return s.lower()
    else: return s.upper()
        

if(__name__) == "__main__":
    s = input()
    s = check(s)
    print(s)