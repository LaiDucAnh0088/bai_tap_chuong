#9.8
def a(x):
    i=1
    s=0
    while i<x:
        if x%i==0: s=s+i
        i+=1
    if x==s: print(x,'là số hoàn hảo')
    else: print(x,'không là số hoàn hảo')
a(17)
