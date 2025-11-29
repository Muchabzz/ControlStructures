# Check if name ends with "a" to identify Polish female name

name = input('Enter name: ')
if name.endswith('a'):
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not a Polish female name')
