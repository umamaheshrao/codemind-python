n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
            print(" ",end="")
    for m in range(1,2*i-1+1):
        print(i,end="")
    print()