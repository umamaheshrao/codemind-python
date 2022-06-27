def ugly_num(n):
    if(n==1):
        return 1
    elif(n%2==0):
        return ugly_num(n//2)
    elif(n%3==0):
        return ugly_num(n//3)
    elif(n%5==0):
        return ugly_num(n//5)
    else:
        return 0
n=int(input())
if(ugly_num(n)):
    print("Ugly Number")
else:
    print("Not Ugly Number")