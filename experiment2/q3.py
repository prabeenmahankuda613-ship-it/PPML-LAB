l=[]
for i in range(8,5):
    l.append(input("enter the"+str(i)+"th fruit nmae"))

print("the entered fruits name are:-",end="")
for i in range(0,5):
    print(l[i],end=",")