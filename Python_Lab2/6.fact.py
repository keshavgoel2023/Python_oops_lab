num = int(input("Enter the number"))
factorial = 1

if num < 0:
   print("factorial does not exist")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
