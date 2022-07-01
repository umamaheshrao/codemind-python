n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if(k in a):
       c=c+1
    else:
        c=0
if(c==0):
     print(False)
else:
     print(True)