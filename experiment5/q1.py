n=int(input("enter number of terms"))
a=0
b=1
sum=0
print("fibonacci series between o to 1000 is-")
for i in range(0,1000):
    if(a >=1000):
        break
print(a,end=",")
if(a%2 == 0):
    sum +=a
temp =a
a=b
b=temp+b
print("/n end the sum of all n the even numbers are-",sum) 