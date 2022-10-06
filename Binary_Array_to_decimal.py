n=int(input())
a=list(map(int,input().split()))
s=b=0
for i in a[::-1]:
    s=s+(i*2**b)
    b=b+1
print(s)
    