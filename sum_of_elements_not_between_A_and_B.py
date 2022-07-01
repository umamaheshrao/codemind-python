n=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
sum=0
for i in a:
    if(i not  in range(n,m+1)):
        sum+=i
print(sum)