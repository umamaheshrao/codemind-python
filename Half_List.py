n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)-1,(n//2)-1,-1):
    print(a[i],end=" ")
for i in range(0,(n//2),1):
    print(a[i],end=" ") 