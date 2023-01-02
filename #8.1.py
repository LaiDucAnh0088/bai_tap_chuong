#8.1
a= int(input('nhap so a: '))
b= int(input('nhap so a: '))
c= int(input('nhap so a: '))
d= int(input('nhap so a: '))
min = a
max = d
if(b<min): min =b
if(c<min): min =c
if(d<min): min=d
if(b>max): max=b
if(c>max): max=c
if(d>max): max=d
print('max: ',max,';min: ',min)
