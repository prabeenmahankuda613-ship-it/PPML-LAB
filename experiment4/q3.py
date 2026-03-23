a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
c=int(input("enter third number:-"))
while(b !=0):
  if(b == 0):
    break
  temp = a
  a=b
  b =temp%b
while(  c !=0):
  if(c == 0):
    break
  temp = c
  a=c
  c =temp%c
  print(a)