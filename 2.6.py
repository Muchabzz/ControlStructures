##Write a program that checks what number was entered from the keyboard and prints one of the messages below. Then run the program and check the following numbers:

number = input('enter number: ')

number = int(number)
if number < 0:
    print(f'number {number} is negative')
elif number == 0:
    print(f'number {number} is 0')
elif number > 0:
    print(f'number {number} is positive')
