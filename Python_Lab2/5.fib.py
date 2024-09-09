n = int(input("Enter the number"))
a = 0
b = 1
next_number = b  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    a, b = b, next_number
    next_number = a + b
print()
