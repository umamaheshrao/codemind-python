s1=input()
s1=s1.lower()
s1=s1.split()
s2=input()
s2=s2.lower()
c=0
s2=s2.split()
for i in s1:
    if i in s2 and s1.count(i)==1 and s2.count(i)==1:
        c+=1
print(c)