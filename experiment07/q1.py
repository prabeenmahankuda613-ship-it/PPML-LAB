m =int(input("enetr the starting of the natural number:-"))
n=int(input("enter the ending of the natural number:-"))

list=[]
for i in range(m,n+1):
    list.append(i)

print("list:",list)
print("sum",sum(list))
print("average",sum(list)/len(list))
print("largest",min(list))
print("smallest",max(list))