n=int(input())
a=list(map(int,input().split()))
k=len(a)
f=0
for i in a:
    if(i==0 or i==1):
        f+=1

if(f==k):
    print(True)
else:
    print(False)