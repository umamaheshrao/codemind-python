n=int(input())
for n in range(1,n+1):
    a=int(input())
    m=a
    rev=0
    r=0
    while a:
        r=a%10
        rev=rev*10+r
        a=a//10
    if(rev==m):
        print("True")
    else:
        print("False")