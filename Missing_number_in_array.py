n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    b=a
    for i in range(1,100):
        if i not in b:
            print(i)
            break