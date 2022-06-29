n=input()
v="0123456789"
c=0
for i in n:
    if(i in v):
        c+=int(i)
print(c)