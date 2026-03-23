para=input("enter the paragraph")
words =para.split()

print("word count:", len(words))

pali_count =0
for w in words:
    if w ==w[::-1]:
     pali_count +=1
print("palindrome count",pali_count)

for w in words :
   print(w[::-1])
