n=int(input())
r=0
m=0
rev=0
while n:
    r=n%10
    if(r>m):
        m=r
    n=n//10
print(m)