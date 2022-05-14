a=int(input())
b=int(input())
for n in range(a,b+1):
    m=n
    sum=0
    r=0
    while(n!=0):
        r=n%10
        sum=sum*10+r
        n=n//10
        if(sum==m):
            print(m,end=' ')