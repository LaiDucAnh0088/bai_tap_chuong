#8.4
import math
a= int(input('nhập độ dài cạnh 1: '))
b= int(input('nhập độ dài cạnh 2: '))
c= int(input('nhập độ dài cạnh 3: '))
p=(a+b+c)/2
S= math.sqrt(p*(p-a)*(p-b)*(p-c))
print('diện tích tam giác là',S)