




def check(s):
    a = list(s)
    cnt_etght = 0
    cnt_six = 0
    for i in a:
        if(i != '6' and i != '8'): return False
        elif(cnt_etght > 2 or (cnt_etght != 0 and cnt_six == 0)): return False

        if(i == '8'): cnt_etght += 1
        else:
            cnt_etght = 0
            cnt_six = 1 
    return cnt_etght <= 2

s = input()
func = lambda x: "YES" if(check(x)) else "NO"
print(func(s))