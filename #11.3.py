#11.3
a=[]
x=str(input('nhap ten con thu: '))
while x!='dung':
    a.append(x)
    x=str(input('nhap ten con thu: '))
    if x=='dung': break
print('so con trong list la:',len(a))
y=str(input('nhap con thu ban muon tim: '))
u= str(y) in a
if u == True: print('co con thu ban can tim')
else: print('khong co con thu ban can tim')
