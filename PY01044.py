




# def merge(a, b):
#     a.sort()
#     b.sort()
#     i, j = 0, 0
#     c = []
#     while(i < len(a) and j < len(b)):
#         if(a[i] == b[j]):
#             print(a[i], end = " ")
#             c.append(a[i])
#             i+=1
#             j+=1
#         elif(a[i] < b[j]):
#             print(a[i], end = " ")
#             i +=1
#         else:
#             print(b[j], end = " ")
#             j += 1
#     while(i < len(a)):
#         print(a[i], end = " ")
#         i += 1
#     while(j < len(b)):
#         print(b[j], end = " ")
#         j += 1
#     print()
#     if(len(c) != 0): print(*c)

# def delete(a):
#     for i in a:
#         if(a.count(i) != 1): 
#             while(a.count(i)!= 1):
#                 a.remove(i)

# s = input().strip()
# s = s.replace(',', ' ')
# s = s.lower()
# a = list(map(str, s.split()))
# delete(a) 
# s2 = input().strip()
# s2 = s2.replace(',', ' ')
# s2 = s2.lower()
# b = list(map(str, s2.split()))
# delete(b)
# merge(a, b)

s = input()
s = s.lower()
s = set(s.split())
t = input()
t = t.lower()
t = set(t.split())

u = s | t
u = list(u) 
u.sort()
print(*u, sep=" ")
u = s & t
u = list(u)
u.sort()
print(*u, sep=" ")