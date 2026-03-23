mylist =["apple","orange","banana"]
print("fruits displayed from last to first inex with in their length:-")
for i in mylist[::-1]:
    print(i,"-length :",len(mylist))
print("/nlist containing reverse of each fruit name:-")
rev=[]
for fruit in mylist:
    rev.append(fruit[::-1])
print(rev)