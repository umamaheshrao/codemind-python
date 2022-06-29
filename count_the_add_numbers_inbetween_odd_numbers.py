n=int(input())
c=[]
k=0
a=list(map(int,input().split()))
for i in range(0,n):
    if(i%2==0):
        c.append(a[i])
for i in c:
    if(i%2!=0):
        k+=1
print(k)