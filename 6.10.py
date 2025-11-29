# Convert dog's age to dog's years

age_in_human_years = int(input('Enter the dog\'s age in human years: '))

if age_in_human_years <= 2:
    age_in_dog_years = age_in_human_years * 10.5
else:
    age_in_dog_years = 21 + (age_in_human_years - 2) * 4

print(f'The dog\'s age in dog\'s years is {age_in_dog_years} years.')
