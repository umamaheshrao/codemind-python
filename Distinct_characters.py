n=input()
n=n.lower()
n=set(n)
n=sorted(n)
for i in n:
    if(i==" "):
        continue
    print(i,end="")