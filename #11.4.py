#11.4
a=[]; sum=0; c=[]
x=str(input('nhap phan tu: '))
while x!='dung':
    a.append(x)
    x=str(input('nhap phan tu: '))
    if x=='dung': break
print('list:',a)
y= int(input('nhap phan tu x: '))
for b in a:
    sum +=int(b)
print('tong cac phan tu trong list:',sum)
u= str(y) in a
if u == True: print('co phan tu',y,'trong list va xuat hien',a.count(str(y)))
elif u == False: print('khong co phan tu',y,' trong list')
if y>int(max(a)): print(y,'lon hon tat ca so trong list')
else:
    for b in a: 
        if y<int(b): c.append(b)
    print('cac so trong list ban dau lon hon',y,': ',c)
