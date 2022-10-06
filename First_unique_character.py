n=input()
n=n.lower()
z=0
for i in n:
    if(n.count(i)==1 and i!=" "):
        print(i)
        z=1
        break
if(z==0):
    print("-1")