n=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
sum=0
f=0
for i in a:
    if(i not  in range(n,m+1)):
        f+=1
        print(i,end=" ")
if(f==0):
    print("-1")