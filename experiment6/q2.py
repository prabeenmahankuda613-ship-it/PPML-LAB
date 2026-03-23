d={}
n=int(input("enter the number of  key value pair:-"))
for i in range(n):
    k=input("enter a key:-")
    v=input("enter a value:-")
    d[k] =v
rev ={}
for k,v in d.items():
    rev[v] =k
print("the original dictionary is:-",d)
print("the new dictionary is:-",rev)