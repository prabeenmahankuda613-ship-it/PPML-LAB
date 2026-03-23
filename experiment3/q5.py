a=int(input("enter first subject mark:-"))
b=int(input("enter second subject mark:-"))
c=int(input("enter third subject mark:-"))
d=int(input("enter fourth subject mark:-"))
e=int(input("enter fifth subject mark:-"))
sum =a+b+c+d+e
per =(sum/250)*100
if(per >= 90 and per <= 100) :
    print ("grade is o")
elif(per >= 80 and per <= 90):
    print("grade is e")
elif(per >= 70 and per <= 80):
        print("grade is a")
elif(per >= 60 and per <= 70):   
     print("grade is b")     
elif(per >= 50 and per <= 70):
     print("grade is c")
elif(per >= 0 and per <= 50):
     print("grade is f")