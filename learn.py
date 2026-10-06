#split

'''
khong phai la tach str thanh cac str ma str thanh cac list
vd s.input().split() (s = "Tran Anh Tuan")
a= list(s) -> a = ['Tran', 'Anh', 'Tuan']
a= list(s[0]) -> a = ['T', 'R', 'A', 'N']
s.input() -> str
s.input().split() -> list
'''
#IF
'''
#pass: bo qua 1 lenh ko thuc hien
#Toan tu 3 ngoi: True if condition else False 
'''
#List
'''
# Khai bao a = []
# Truy cap phan tu: 
    + Neu chi so i >=0 se la duyet tu trai sang phai (0, len(a) - 1)
    + Neu chi so i < 0 se la duyet tu phai sang trai (-1, len(a))
# Constructor a = list(s)
# Duyet
# Thay doi gia tri nhu C++
# Them phan tu
    + a.append(): them cuoi list
    + a.insert(i, vl): them o vi tri i
    + list a + b: noi list b vao cuoi list a
# Xoa phan tu
    + a.pop(): xoa phan tu o cuoi -> Tra ve phan tu bi xoa
    + a.pop(i): xoa phan tu o vi tri i -> Tra ve phan tu bi xoa
    + del a[i]: xoa phan tu o vi tri i -> Ko tra ve gia tri
    + a.remove(x): xoa phan tu co gia tri x dau tien 
    + a.clear(): xoa het tat ca ve nhau
# Sao chep list: b = a * n voi (a, b la list | n la so ban sao)
# Noi list: c = a + b
# Tim kiem phan tu: 
    + in tra ve true neu x co trong list
    + not in tra ve true neu x ko co trong list
# extend list:
    + a.extend(b): a += b (a, b la list)
# Copy: b = a.copy() | tao b la ban sao cua a 
# a.count(x): dem so lan xuat hien cua x trong list a
# a.index(x): tra ve chi so cua x dau tien trong list
# a.reverse(): Lat a
# a.sort(): sap xep
# sorted(a): sap xep 
# min(a): tra ve phan tu nho nhat
# max(a): tra ve phan tu lon nhat
# sum(a): tra ve tong tat ca phan tu o list

# list slicing: Lay phan tu cua 1 list theo tu vi tri x cho den vi tri i
    + Khuon lenh: a[start: end: step]
        VD: a = [4, 3, 2, 1] -> a[2, 4, 1] ->['2']
    + a.reverse() = a[::-1]
    + Thay/xoa 1 khoang = a[l:r:] = [1, 2, 3, ...]
# Lambda function: Giong ham nhung chi chua 1 bieu thuc duy nhat va khong co return
    + Khuon lenh: func = lambda x...: x*2... -> func(2) = 4 || func = (lambda x...: x*2...)(10)
    + Ket hop voi map: map(func, list) -> cac phan tu deu phai dap func
    + Ket hop voi filter: filter(func, list) -> chon cac phan tu tm dk cua func
# List Comprehension
    + b = [i for i in a] -> tao ra list theo condision
# Unpacking list/str/range
    + x, y, z, _, _ = a[] -> x, y, z se lay 3 gia tri dau cua list ko lay phan tu thua
    + x, y, *z = a[] -> x, y se lay 2 gia tri dau con lai la luu vao z
# zip(list a, list b......)
# enumerate(danh sach): tu dong lay index
itertools tang toc duyet vong lap
thu vien json, numpy
'''
#String
'''
# str khong the thay doi duoc(immutable)
# str.isdigit: kiem tra str co toan la so ko | dung -> True
# str.isalpha: kiem tra str co toan la chu cai ko | dung -> True
# str.isalnum: kiem tra trong str chi chua toan so or toan chu | dung ->True
# str.islower, str.isupper: kiem tra str viet thuong hay hoa
# ord('kitu'): Tra ve ma Ascii
# chr(x): Tra ve ki tu co ma Ascii tuong ung
# str.rjust(do rong cua chuoi, ki tu them vao)
# str.ljust()
# str.center()
# str.strip(): xoa khoang trang du thua
# str.startswith(x): Kiem tra chuoi co bat dau bang 1 chuoi con nao do hay ko -> True/False
# str.endswith(x): Kiem tra chuoi co ket thuc bang 1 chuoi con nao do hay ko -> True/False
# str.find(x): Tim 1 chuoi con x tra ve vi tri dau tien | khong thay -> -1 
# str.rfind(x): Tim 1 chuoi con x tra ve vi tri cuoi | khong thay -> -1
# str.count(x): Dem chuoi con x
# str.format(x, y, ....): Dinh dang vd '{} {}'.format(x, y)
# str slicing nhu list
# "ki tu de noi".join(list)): Noi cac phan tu trong list thanh chuoi <=> str.join(sep, list)
# str.replace("xau cu","xau muon doi", so luong muon doi)
# str.upper(): Chuyen tat ca thanh hoa
# str.lower(): Chuyen tat ca thanh thuong
# str.capitalize(): Chi viet hoa chi cai dau cua ca xau
# str.swapcase(): Doi thuong thanh hoa, hoa thanh thuong 
# str.title(): Viet hoa chu cai dau cua moi tu trong Xau, con lai la thuong

'''
#Tuple
'''
# Tinh chat: Giong list khac ko the thay doi( not insert, delete and sua)
# Khuon len khai bao: a = (x, y, ....) (co the ep str/list bang cach tuple(str/list))
# Tuy Tuple ko the thay doi dc gia tri nhung cai object trong co the thay doi bang cach tuple[x][y] = ....
# Tuple concatenation: Noi 2 Tuple(c = a + b)
# Tuple repetition: Nhan ban Tuple(b = a* n)
# sap xep: sorted(Tuple) -> tra ve list(Neu muon dung sort -> chuyen tuple ve list)
# Cac ham nhu list
'''
# Map and filter
'''
# Map se ap dung 1 function cho tat ca cac phan tu o iterable
# Khuon lenh cua map: map(function, iterable1, interable2 ) -> tra ve doi tuong thuoc lop map
# Filter se dung 1 function de lap cac phan tu t/m o iterable
'''
# Sort
'''
# Khuon len: a.sort(key, reverse) | reverse = True -> sap xep nguoc| key chua ham
# from functools import cmp_to_key: them thu vien de co the viet ham cmp
'''
# Thu vien SYS
'''
# Toi uu nhap: a = sys.stdin.readline()

'''
# Thu vien bisect
'''
# bisect_left(list, x): Phan tu dau tien lon hon bang x
# bisect_right(list, x): Phan tu dau tien lon hon bang x
'''
# Set
'''
# Set luu khong co thu tu
# Set luu cac phan tu ko trung nhau
# Set ko the truy cap qua chi so
# Set co the xoa va them
# Set chi luu cac phan tu khong the thay doi duoc -> set ko luu duoc list
# Khuon lenh: set = {..., ..., ....}
# Set constructor: set = set(list/str/...)
# Cac ham trong Set:
    + Set.add(x): Them phan tu x vao set | Tu loai bo trung
    + Set.update([..., ...]): Them nhieu phan tu
    + Set.pop(): Xoa phan tu random
    + Set.remove(x): Xoa phan tu co val = x -> x phai ton tai trong Set
    + Set.discard(x): Xoa phan tu co val = x
    + Set.clear(): Xoa tat ca moi thu ve nhau
    + len(s): Tra ve so luong phan tu
    + Duyet: Use For x
    + Tim kiem: Use in -> O(1)
    + s.union(t): tim hop cua 2 tap hop s va t -> Tra ve 1 tap hop = s | t
    + s.intersection(t): tim giao cua 2 tap hop s va t -> Tra ve 1 tap hop = s & t
    + s.difference(t): Tim hieu cua 2 tap hop s va t -> Tra ve 1 tap hop = s - t
    + s.symmetric_difference(t): Tim hop cua s - t ve t - s -> Tra ve 1 tap hop = s ^ t
    + s.isdisjoint(t): Kiem tra s ko giao t hay ko -> Neu ko giao tra ve True.
    + s.issubset(t): Kiem tra s co phai con cua t ko -> Neu co tra ve True
    + s.issuperset(t): Kiem tra s co phai bo t ko -> Neu co tra ve True 
'''
# Dictionary = map
'''
# Key trong dict ko luu trung
# Key luu cac kieu du lieu ko the thay doi
# Khuon lenh: Dictionary = { Key1: value1, Key2: value2,....}
# dict(list/tuple): Chuyen tu list/tuple sang Dictionary
# dict(zip(a, b)): Cac phan tu trong a se la key va cac phan tu trong b se la value tuong ung
# dict.fromkeys(list key, default val): Khoi tao cac key deu co value = default val
# mp[key] = value = mp.get(key)
# mp.keys(): Tra ve 1 day key
# mp.values(): Tra ve 1 day value
# mp.items(): Tra ve 1 day key va value
# mp[key] = value: gan (key, value)
# mp.pop(key): xoa dict | phai co key ko se loi | Tra ve value
# del mp[key]: xoa dict | ko bao loi neu key ko ton tai| Ko tra ve value
# key in mp: Kt xem key co ton tai trong mp ko O(1)(chi voi key)
# a.update(b): Tron dict a voi dict b
# dict comprehension: {key: vaule for vaule in a}
# from collections import Counter -> dem nhanh moi phan tu trong list xuat hien bao nhieu lan |sx theo thu tu tang dan

'''
# Mang 2 chieu = nestedList
'''
# Ban chat list chua cac list
# Nhap:
    +C1:
        for i in range(n)
        b = list(map(int, input().split()))
        a.append(b)
    +C2:
        a = [0]* n
        for i in range(n):
            a[i] = list(map(int, input().split()))

# Duyet: Giong C/C++
# Trai NestedList thanh list: b = [x for j in a for x in j] 
'''

import json

if(__name__) == '__main__':
    x = '{ "name":"Tuan", "age": 20, "city":"BacGiang"}'
    y = json.loads(x)
    for a, b in y.items():
        print(a,":", b)
