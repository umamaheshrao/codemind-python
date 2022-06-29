n=int(input())
a=list(map(int,input().split()))
s=0
import math
for i in a:
    p=int(math.sqrt(i))
    if(i==p*p):
        s+=i
print(s)