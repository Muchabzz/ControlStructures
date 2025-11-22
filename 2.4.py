###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = input('first number: ')
number2 = input('second number: ')
operator = input('operator: ')

if operator == '+':
    result = int(number1) + int(number2)
elif operator == '-':
    result = int(number1) - int(number2)
elif operator == '*':
    result = int(number1) * int(number2)
elif operator == '/':
    result = int(number1) / int(number2)

# print result
print(f'{number1} {operator} {number2} = {result}')