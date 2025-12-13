# Convert decimal number to binary
number = int(input("Enter decimal number: "))
original = number
binary = ""

while number > 0:
    remainder = number % 2             #number % 2 daje resztę z dzielenia przez 2, czyli 0 albo 1.
    binary = str(remainder) + binary
    number = number // 2

print(f"{original}(10) = {binary}(2)")
