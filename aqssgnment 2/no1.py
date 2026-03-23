#WAP to print the the second largest and second smallest element in a list of 10 integers witout using sort function
arr=[]
x=int(input("enter no of elements"))
for x in range(x):
    m=int(input("Enter the elemment"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
       if arr[k]>arr[k+1]:
           arr[k],arr[k+1]=arr[k+1],arr[k]
print("the sorted array is:")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("second largest element is",second_largest)
print("seconmd smallest number is",second_smallest)