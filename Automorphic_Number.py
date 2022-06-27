n=int(input())
t=n*n
r=0
r=t%10
m=t%100
s=t%1000
if(r==n or s==n or m==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")