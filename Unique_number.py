n=int(input())
f=0
c=0
t=n
for i in range(1,10):
    f=0
    t=n
    while t!=0:
        r=t%10
        if(r==i):
            f=f+1
        t=t//10
    if(f>1):
        c=c+1
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")