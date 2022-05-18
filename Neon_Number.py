t=int(input())
sum=0
product=1
n=t*t
while n>0:
    r=n%10
    sum+=r
    n=n//10
if sum==t:
    print("Neon Number")
else:
    print("Not Neon Number")