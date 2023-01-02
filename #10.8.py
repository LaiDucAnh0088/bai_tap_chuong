#10.8
import calendar
e= ('thứ hai','thứ ba','thứ tư','thứ năm','thứ sáu','thứ bảy','chủ nhật')
a= int(input('Nhập ngày: '))
b= int(input('Nhập tháng: '))
c= int(input('Nhập năm: '))
print('Ngày tháng năm vừa nhập: ',a,'-',b,'-',c)
if calendar.isleap(c)==True: print('Năm',c,'là năm nhuận')
else: print('Năm',c,'không là năm nhuận')
d= int(calendar.weekday(c,b,a))
print(a,'-',b,'-',c,' là',e[d])
f= str(calendar.monthrange(c,b)).split(' ')
print('Số ngày trong tháng',b,'là:',str(f[1]).replace(')',' '))
