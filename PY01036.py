





t = int(input())
while(t > 0):
    n = int(input())
    st = 0
    if(n%2 == 0): st = 2
    else: st = 1
    sum = 0
    for i in range(st, n +1 , 2):
        sum += 1/i
    print('{:6f}'.format(sum))
    t-= 1