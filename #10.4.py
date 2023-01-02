#10.4
import math
a= lambda x, n: math.pow((x*x+x+1),n)+ math.pow((x*x-x+1),n)
print(a(2,3))