
num = int(input("Enter the number"))
flag = True

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
            break

    if flag:
        print(num, "Prime number")
    else:
        print(num, "Not a prime number")