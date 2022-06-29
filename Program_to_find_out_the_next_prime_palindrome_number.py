def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
def rev(n):
    re=0
    s=n
    while(n!=0):
        r=n%10
        re=re*10+r
        n=n//10
    if(s==re):
        return 1
    else:
        return 0
n=int(input())
re=0
for i in range(n+1,100000):
     if(rev(i)):
         if(prime(i)):
             print(i)
             break
 
 
 