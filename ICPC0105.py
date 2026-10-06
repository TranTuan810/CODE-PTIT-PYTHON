




if(__name__) == '__main__':
    t = int(input())
    while(t > 0):
        s = input()
        a = list(s)
        c_res = ""
        res = -1
        for i in a:
            if(i.isdigit()):
                c_res += i
            else:
                if(len(c_res) != 0):
                    res = max(res, int(c_res))
                    c_res = ""   
                     
        if(len(c_res) != 0):
            res = max(res, int(c_res))
            c_res = ""

        print(res)
        t -= 1