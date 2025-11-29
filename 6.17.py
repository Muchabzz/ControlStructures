# Convert time in 24-hour format to 12-hour format

time_24hr = input('Enter time (24-hour format): ')
hours, minutes = map(int, time_24hr.split(':'))

period = 'am'
if hours >= 12:
    period = 'pm'
    if hours > 12:
        hours -= 12

print(f'Time in 12-hour format: {hours}:{minutes:02d}{period}')
