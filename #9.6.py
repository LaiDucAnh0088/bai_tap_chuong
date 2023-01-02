#9.6
x= int(input('nhap so: '))
def f(n):
    i=2; a=0
    while i<n:
        if(n%i!=0): a=''
        else: 
            a='khong'
            break
        i+=1
    if n<=1: a='khong'
    return print(n,a,'la so nguyen to')
f(x)