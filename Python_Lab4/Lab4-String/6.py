vowels = "aeiouAEIOU"
string = input("Enter a string to count vowels: ")
count = sum(1 for char in string if char in vowels)
print(count)
