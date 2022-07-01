n=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
for i in a:
    f=0
    if(max(a) not in range(n,m+1)):
        f+=1
        print(max(a))
        break
if(f==0):
    print("-1")