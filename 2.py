n =  int(input("Enter the value of n"))

for i in range(0,n,1):  
   for j in range(i,n):
      print("1",end = "")
   for j in range(1):
      print("*",end = "")
   for j in range(i):
      print("3",end = " ")
   for i in range(1):
      print("*", end =" ")
   print()
for i in range(n):  
   for j in range(i):
      print("2",end = "")
   for i in range(1):
      print("*", end ="")

   print()



