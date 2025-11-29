# 25% discount for purchasing over two products

num_products = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))

if num_products > 2:
    total = num_products * product_price * 0.75  # 25% discount
else:
    total = num_products * product_price

print(f'Amount to pay: {total}')
