n = int(input("enter a number:-"))
temp1 =n
temp2 =0
while(temp1 !=0):
    temp2=(temp2*10)+(temp1%10)
if(n == temp2):
    print(f"{n} is a palindrome")
else:
       print(f"{n} is  not a palindrome")
