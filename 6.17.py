# Convert time in 24-hour format to 12-hour format

time24 = input("Enter time (24-hour format): ")

hour, minute = time24.split(":") #split(":") dzieli zapis „hh:mm” na godzinę i minuty.
hour = int(hour)

if hour == 0:
    hour12 = 12
    period = "am"
elif hour < 12:
    hour12 = hour
    period = "am"
elif hour == 12:
    hour12 = 12
    period = "pm"
else:
    hour12 = hour - 12
    period = "pm"

print(f"Time in 12-hour format: {hour12}:{minute}{period}")
