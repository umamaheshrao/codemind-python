n=int(input())
m=n
rev=0
import math
d=int(math.log10(n)+1)
while(m!=0):
    r=m%10
    rev=rev+r**d
    d=d-1
    m=m//10
if(rev==n):
    print(True)
else:
    print(False)