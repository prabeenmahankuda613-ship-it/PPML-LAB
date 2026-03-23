a=int(input("enetr the first side:-"))
b=int(input("enter the second side:-"))
c=int(input("enter the third side :-"))                                           
sum=a+b+c
s=sum/3
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area is",area)
print("perimeter is",sum)