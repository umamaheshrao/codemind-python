n=int(input())
k=0
a=list(map(int,input().split()))
for i in range(0,n):
    if(a[i]%2!=0):
        k=i
print(k)