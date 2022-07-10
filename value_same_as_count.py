n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if(a.count(i)==i and i not in b):
        b.append(i)
for i in b:
    c+=1
print(c)