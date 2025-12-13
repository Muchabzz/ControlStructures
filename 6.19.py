# Survey Program
print("SURVEY")
print("SURVEY")

cs = input("Are you interested in computer science? (y/n): ") == "y"
games = input("Do you like playing computer games? (y/n): ") == "y"
instagram = input("Do you have an Instagram account? (y/n): ") == "y"

print()
print("SURVEY RESULTS")

print("Interested in computer science:", "Yes" if cs else "No")
print("Playing computer games:", "Yes" if games else "No")
print("Has an Instagram account:", "Yes" if instagram else "No")
