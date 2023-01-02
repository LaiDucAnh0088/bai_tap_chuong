#9.1
def sign(x):
    if x<0: x=-1
    if x>0: x=1
    if x==0: x=0
    return str(x)
print(sign(77))
