n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
s=0
for i in a:
    if(a.count(i)==i and i not in b):
        b.append(i)
        s+=1
        c+=i
if(c==0):
    print(-1)
else:
    m=c/s
    print("{:.2f}".format(m))