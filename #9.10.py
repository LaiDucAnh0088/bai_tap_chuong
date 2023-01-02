#9.10
p1=0; i=0; p= [0,1]
n= int(input('Nhập n: '))
if n >1:
    while i<=n:
        p1= p[i]+p[i+1]
        p.append(p1)
        i+=1
print(p[n])