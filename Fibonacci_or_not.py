n=int(input())
a=0
b=1
c=0
for i in range(3,n+1):
    f=a+b
    if(f==n):
        c=1
    a=b
    b=f
if(c==1):
    print(True)
else:
    print(False)