#9.9
d= lambda a,b: (a+b)*2 
e= lambda r: 2*r*3.14
f= lambda a,b: a*b
g= lambda r: r*r*3.14
x= int(input('nhap so canh a: '))
y= int(input('nhap so canh b: '))
z= int(input('nhap so bán kinh r: '))
print('Chu vi hình chữ nhật: ',d(x,y),'\n' 
'Diện tích hình chữ nhật: ',f(x,y),'\n' 
'Chu vi hình tròn: ',e(z),'\n' 
'Diện tích hình tròn: ',g(z))
