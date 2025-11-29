# Convert decimal number to binary
decimal_number = int(input('Enter decimal number: '))
binary_rep = []

while decimal_number > 0:
    binary_rep.append(str(decimal_number % 2))
    decimal_number //= 2

binary_rep.reverse()  # Reverse to get the correct order
binary_str = ''.join(binary_rep)

print(f'{decimal_number} (10) = {binary_str} (2)')
