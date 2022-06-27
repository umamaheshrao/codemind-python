n=int(input())
t=n*n
r=0
re=0
m=0
rev=0
k=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
re=rev*rev
while re:
    k=re%10
    m=m*10+k
    re=re//10
if(t==m):
    print(True)
else:
    print(False)