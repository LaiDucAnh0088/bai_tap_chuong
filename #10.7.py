#10.7
s= str(input('Nhập chuỗi s: \n'))
s_sub= str(input('Nhập chuỗi con s_sub: \n'))
s_find= str(input('Nhập chuỗi tìm s_find: \n'))
s_replace= str(input('Nhập chuỗi thay thế s_replace: \n'))
s= s.strip()
print('Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi: ',s)
print('Số lần s_sub xuất hiện trong s: ',s.count(s_sub,0,100))
print('Chuỗi s sau khi tìm kiếm và thay thế: ',s.replace(s_find,s_replace))