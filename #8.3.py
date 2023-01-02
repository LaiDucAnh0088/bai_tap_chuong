#8.3
a= int(input('nhap he so a: '))
b= int(input('nhap he so b: '))
if(b==0):
    x=0
    print('phuong trinh co nghiem: ',x)
else:
    if(a==0):
        print('phuong trinh vo nghiem')
    else:
        x= -b/a
        print('phuong trinh co nghiem la: ',x)