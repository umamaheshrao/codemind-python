n=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(0,n):  
    sum+=a[i]
print(sum)