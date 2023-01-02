#10.5
s= str(input('Nhập mã: '))
if s.isdigit()==True: 
    if len(s)==6: print(True)
    else: print(False)
else: print(False)