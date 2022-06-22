x,y=map(int,input().split())
tol=(1*x)+(2*y)
if(x%2==0and y%2==0):
    print("YES")
elif(x%2!=0and y%2!=0):
    print("NO")
elif(x==0and y%2!=0):
    print("NO")
elif(x==0and y%2==0):
    print("YES")
elif(tol%2==0):
    print("YES")
else:
    print("NO")