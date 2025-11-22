###
# Credit card payment 
#
account_balance = 500
total_payment = input('your payment: ')

if int(total_payment) <= account_balance:
    print('Payment completed')
else:
    print('No funds')