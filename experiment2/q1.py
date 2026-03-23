import sys
p= float(input("enter the principal amount:- "))
r=float(input("enter the rate of amount:-"))
t=float(input("enter the time period of the year:-"))
si=(p*t*r)/100
print("simple interest is:-",si)
a=p*(1+r/100**t)
ci=a-p
print("the compound interst is:-",si)