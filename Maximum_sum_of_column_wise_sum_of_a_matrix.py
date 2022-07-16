n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
s=0
max=0
for j in range(m):
    for i in range(n):
        s+=a[i][j]
    if(s>max):
        max=s
    s=0
print(max)
