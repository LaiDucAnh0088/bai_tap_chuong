a= int(input('Nhập cân nặng (kg): '))
b= int(input('Nhập chiều cao (m): '))
BMI= a/(b*b)
if(BMI< 18.5): a='gầy'
if(18.5<=BMI<25): a='bình thường'
if(BMI>=25): a='thừa cân'
print('Chỉ số BMI: ',BMI,'; bạn thuộc dạng',a)
