n=int(input())
c=0
sum=0
avg=0
a=list(map(int,input().split()))
for i in a:
    sum+=i
avg=sum//n
for i in a:
    if(avg<=i):
        c+=1
print(c)