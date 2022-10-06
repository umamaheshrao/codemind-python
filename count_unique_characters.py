n=input()
n=n.lower()
z=0
for i in n:
    if(n.count(i)==1 and i!=" "):
        z+=1
      
if(z==0):
    print("-1")
else:
    print(z)
