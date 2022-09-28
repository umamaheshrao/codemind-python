def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return n
n=int(input())
a=[]
c=0
for i in range(2,n):
    for j in range(2,n):
        if(prime(i)*prime(j)==n):
            a.append(i)
            a.append(j)
            c+=1
            break
a=set(a)
if(c>=1):
    print(*a)
else:
    print(-1)