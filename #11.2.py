#11.2
a=[]
b=[]
y=input('nhap nhom: ')
while y!='dung':
    if y=='co':
        x=str(input('Nhap ten thanh vien: '))
        while x!='dung':
            a.append(x)
            x=str(input('Nhap ten thanh vien: '))
            if x== 'dung':
                break
        b.append(a)
    y=str(input('nhap nhom: '))
    if y=='dung': break
print('danh sach cua ban: ',b ,'\n'
'day la doi truong trong team te nhat: ',b[int(len(b))-1][0])