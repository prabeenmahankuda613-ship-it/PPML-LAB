#wap to calculate of a number using recursion
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int(input("enter the number"))
if(n<0):
    print("its a Negative number")
else:
    print("Factorial of",n,"is",factorial(n))
