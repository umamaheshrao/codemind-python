m,n,=map(int,input().split())
a=[]
for i in range(m):
    b=list(map(int,input().split()))
    a.append(b)
s=0
max=0
for i in range(m):
    for j in range(n):
        s=s+a[i][j]
    if(s>max):
        max=s
    s=0
print(max)
