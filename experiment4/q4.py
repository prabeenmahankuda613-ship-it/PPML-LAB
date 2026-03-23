n = int(input("enter a number:-"))
sum =0
while(n >= 0):
    r = n% 10
    sum += r
    n //= 10
print("sum of digits =",sum)