n=int(input())
n1=int(input())
r=0
re=0
sum=0
sum1=0
for i in range(1,n):
    if n%i==0:
        sum+=i
for j in range(1,n1):
    if n1%j==0:
        sum1+=j
if(sum==n1 and sum1==n):
    print("Amicable")
else:
    print("Not Amicable")