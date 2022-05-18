n=int(input())
sum=0
product=1
while n>0:
    r=n%10
    sum+=r
    product*=r
    n=n//10
res=product-sum
print(res)