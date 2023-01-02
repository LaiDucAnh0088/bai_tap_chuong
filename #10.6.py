#10.6
import math
a= int(input('nhap he co so a: '))
b= int(input('nhap he co so b: '))
c= int(input('nhap he co so c: '))
if c==0: 
    if a==0: print('Phương trình có 1 nghiệm: ',0)
    else: 
        x1= -b/a  
        x2= 0
        print('Phương trình có nghiệm: \n '
            'x1=' ,x1,'\n'
            'x2= ',x2)
else: 
    if a==0: print('Phương trình có 1 nghiệm: ',-b/c)
    else:
        x=b*b - 4*a*c
        if x>0:
            x1= math.sqrt(x)/(2*a)
            x2= -x1
            print('Phương trình có nghiệm: \n '
            'x1=' ,x1,'\n'
            'x2= ',x2)
        if x<0: print('Phương trình vô nghiệm')
        if x==0: print('Phương trình có 1 nghiệm: ',-b/(2*a))