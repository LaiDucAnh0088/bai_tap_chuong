#11.5
a=[]; b=[]; c=[]
x=str(input('nhap phan tu: '))
while x!='dung':
    a.append(x)
    x=str(input('nhap phan tu: '))
    if x=='dung': break
print('list:',a)
for y in a:
    i=2; u=0
    if int(y)>1:
        i=2; u=0
        while i < int(y):
            if int(y)%i!=0: 
                i+=1
                u=1 
    if u==1: b.append(y)
print('cac so nguyen to',b)
