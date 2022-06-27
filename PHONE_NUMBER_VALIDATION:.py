n=int(input())
m=0
s=0
while n:
    r=n%10
    s=s+1
    n=n//10
    m=r
if(s<10 or m==0):
    print("Invalid")
else:
    print("Valid")