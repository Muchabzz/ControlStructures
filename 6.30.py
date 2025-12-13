# Print a lottery coupon (numbers 1 to 49)
for row in range(1, 8):  # wiersze od 1 do 7
    num = row
    while num <= 49:
        print(num, end=' ')
        num += 7  # kolejna liczba w tym wierszu jest o 7 większa
    print()  # nowa linia po każdym wierszu