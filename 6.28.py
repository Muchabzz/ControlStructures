# Print the first 20 Fibonacci numbers
a, b = 0, 1
print(a, end=' ')
for _ in range(1, 20):
    print(b, end=' ')
    a, b = b, a + b
