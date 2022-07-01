n=int(input())
a=list(map(int,input().split()))
b=sum(a)
c=b/n
print("{:.2f}".format(c))