def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
n=int(input())
for i in range(n):
    m=int(input())
    k=l=m
    c1=c2=0
    while(1):
        if(prime(k)):
            a=k
            break
        k+=1
        c1+=1
    while(1):
        if(prime(l)):
            b=l
            break
        l=l-1
        c2+=1
    if(c1>=c2):
        print(b)
    else:
        print(a)
