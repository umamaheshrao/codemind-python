n=int(input())
a=list(map(int,input().split()))
c=1
for i in a:
    if(a.count(i)==i):
        max=i
for i in a:
    if(a.count(i)==i):
        min=i
        break
    elif(a.count!=i):
        max=0
        min=0
        c=0
if(c==1):
    print(min,max)
else:
    print(-1)