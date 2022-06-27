n=int(input())
r=0
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)