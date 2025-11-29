# Check point position in the coordinate system

x = int(input('Enter x coordinate: '))
y = int(input('Enter y coordinate: '))

if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the fourth quadrant')
elif x == 0 and y == 0:
    print(f'Point P({x},{y}) is at the origin')
elif x == 0:
    print(f'Point P({x},{y}) is on the y-axis')
else:
    print(f'Point P({x},{y}) is on the x-axis')
