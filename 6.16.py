# Washing machine total time calculation

washing_product = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ') == 'y'
extra_spin = input('Extra spin? (y/n): ') == 'y'

washing_time = {'j': 40, 'u': 70, 's': 20}
total_washing_time = washing_time.get(washing_product, 0)

if extra_rinse:
    total_washing_time += 15
if extra_spin:
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes')
