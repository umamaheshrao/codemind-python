n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
k=0
for i in a:
    if(i%2!=0):
        b.append(i)
    else:
        c.append(i)
        
print(*(b+c))