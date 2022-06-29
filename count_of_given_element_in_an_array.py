n=int(input())

a=list(map(int,input().split()))
m=int(input())
for i in range(0,n):
    print(a.count(m))
    break