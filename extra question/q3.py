def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
n=int(input("eneter the number:-"))
print(f"the sum of first {n} natural numbers{sum(n)}")