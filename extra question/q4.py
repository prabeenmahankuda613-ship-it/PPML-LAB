def reverse(n):
    if len(n) == 0:
        return n
    return reverse(n[1:])+n[0]
n=input("enter a string")
print("its reverse is",reverse(n))
    
    