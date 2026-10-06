


if __name__ == '__main__':
    s = input()
    a, b, c, d, e = map(str, s.split())
    if(int(a) + int(c) == int(e)): print("YES")
    else: print("NO")