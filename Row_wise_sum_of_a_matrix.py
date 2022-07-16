m,n,=map(int,input().split())
a=[]
for i in range(m):
    b=list(map(int,input().split()))
    a.append(b)
s=0
max=0
c=[]
for i in range(m):
    for j in range(n):
        s+=a[i][j]
    c.append(s)
    s=0
print(*c)
