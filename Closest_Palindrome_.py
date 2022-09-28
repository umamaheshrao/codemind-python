def pal(n):
    t=n
    p=0
    while(t):
        r=t%10
        p=p*10+r
        t=t//10
    if(p==n):
        return True
    else:
        return False
n=int(input())
k=0
s=0
d=n
while(True):
    d=d+1
    if(pal(d)):
        k=d
        break
s1=n
while(True):
    s1=s1-1
    if(pal(s1)):
        s=s1
        break
if(n-k>s-n):
    print(k)
elif(n-k<s-n):
    print(s)
else:
    print(s,k)
    
    
    
    