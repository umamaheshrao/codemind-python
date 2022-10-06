n=input()
n=n.lower()
z=0
a=[]
for i in n:
    if(n.count(i)==1 and i!=" "):
        a.append(i)
        z=1
a=sorted(a)
x="".join(a)
if(z==0):
    print("-1")
else:
    print(x)
    