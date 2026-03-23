#wap to check whether a string is symmetrical or palindrome
x=int(input("enter a string"))
z=(str(str(x)[::-1]))
if x==z:
    print("it is palindrome")
else:
    print("it is not a palindrome ")