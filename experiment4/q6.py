n = int(input("enter a number:-"))
if n<0 :
    print("factrioal not defined for negative numbers")
else:
    fact=1
    i=1
    while i<n:
        fact *=i
        i+=1
        print("factorial -:",fact)

   
