



from math import *

s = input()
a = list(s)
a = a[::-1]
b = []
sum = 0
for i in range(len(a)):
    sum += int(a[i]) * int(pow(2, i%3))
    if(i % 3 == 2):
        b.append(sum)
        sum = 0
if(sum != 0): b.append(sum)
b = b[::-1]
print(*b, sep = "")