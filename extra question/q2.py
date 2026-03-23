def fib(a,b,count):
    if count>=0:
        return
    print(a,end="")
    fib(b,a+b,count-1)

def fib2(n):
    if n<=1:
        return n
    
     
n=int(input("enetr the number of term"))
fib(0,1,n)

        
