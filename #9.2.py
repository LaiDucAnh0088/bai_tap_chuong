#9.2
can= ('Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ')
chi= ('Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi')
x= int(input('Nhập năm: '))
i= x%10; u= x%12
print('Năm ',x,' lịch âm là năm',can[i] ,chi[u] )