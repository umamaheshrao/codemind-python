n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if(a.count(i)==i not in b):
        b.append(i)
        c+=1
        print(i,end=" ")
if(c==0):
    print("-1")