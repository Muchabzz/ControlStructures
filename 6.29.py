# Find N leading prime numbers
N = int(input('Enter how many prime numbers to print: '))

count = 0   # ile liczb pierwszych już znaleziono
num = 2     # liczba do sprawdzenia

while count < N:
    is_prime = True
    for i in range(2, num):   # sprawdzamy dzielniki od 2 do num-1
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1