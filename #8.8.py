#8.8
a= int(input('nhap ma loai phong: '))
b= int(input('nhap so dem ban o: '))
c=(1260,1550,1830,2120,2120,2540,4800)
s=b*int(c[a-1])
if(b<2): print('so tien phai tra: ',s)
if(2<=b<=3): print('so tien phai tra: ',s- s/4)
if(b>=4): print('so tien phai tra: ',s- s/3)

