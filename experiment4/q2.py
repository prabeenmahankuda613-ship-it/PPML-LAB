import math
n = int(input("enter a number:-"))
i=2
while(i <= math.sqrt(n)):
    print(n,"is not a prime number")
    break
print(n,"is not a palindrome")