




n = input()
a = list(n)
point = -3
while(point > -1*len(a)):
    a[point: point:1] = [',']
    point -= 4

print(*a, sep = "")

# a[-3:-3:1] -> a[-3, -2, 1]
# a[-3:-3:-1] -> a[-3, -4, -1]

