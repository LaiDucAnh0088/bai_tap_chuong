a = [1, 2, 3]
b = []
for n in a:
    i =2
    while i<a[0]:
        if a%i !=0:
            b.append(int(n))
            print(b)
        else:
            break
        i +=1
print(b)