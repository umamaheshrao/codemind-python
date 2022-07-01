n=int(input())
a=list(map(int,input().split()))
f=0
for i in a:
    if(i%2==0):
        f+=1

if(f==n):
    print(True)
else:
    print(False)