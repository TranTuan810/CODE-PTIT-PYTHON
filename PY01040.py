


def translate(a):
    # devide
    s1 = a[:len(a)//2]
    s2 = a[len(a)//2:]
    # Rotate
    sum1, sum2 = 0, 0
    for i in range(len(s1)):
        sum1 += ord(s1[i]) - ord('A')
    for i in range(len(s2)):
        sum2 += ord(s2[i]) - ord('A')
    for i in range(len(s1)):
        s1[i] = chr((ord(s1[i]) - ord('A') + sum1) % 26 + ord('A')) 
    for i in range(len(s2)):
        s2[i] = chr((ord(s2[i]) - ord('A') + sum2) % 26 + ord('A'))
    #Merge 
    for i in range(len(s1)):
        s1[i] = chr((ord(s1[i]) - 2*ord('A') + ord(s2[i]))%26 + ord('A'))
    return s1


t = int(input())
while(t >0):
    s = input()
    a = list(s)
    print(*translate(a), sep = "")
    t -=1