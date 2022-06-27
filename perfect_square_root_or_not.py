n=int(input())
s=0
for i in range(1,int(n**0.5)+1):
    if(i*i==n and n%i==0):
        s=1
if(s==1):
    print(True)
else:
    print(False)
    