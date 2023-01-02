#8.5
x= int(input('nhap so nam: '))
if(x%4==0):
    if(x%100==0): print('day khong la nam nhuan')
    else: print('day la nam nhuan')
else: print('day khong la nam nhuan')
if(x%400==0): print('day la nam nhuan')
