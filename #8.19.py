#8.19
a= int(input('nhap so cuoi: '))
i=0; n=''
while (i<a):
    i=int(input('nhap so: '))
    n += str(i)
kq=''
for ch in n:
    kq= ch + kq
for ch in kq:
    if(int(ch)%2!=0):
        print(ch, end ='')
    


