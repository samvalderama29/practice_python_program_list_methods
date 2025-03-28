# Prog09: capitalize() makes the first letter of the string, capital letter. And all other letter in small case.
#         Create a program that do the same functionality without using capitalize() function.

# Print message that explains the purpose of the program
print("Make the first letter capital without using capitalize()")

# Get user input
word = input("Enter a word: ")

# Use if-else logic to check if the input is not empty
if word:
    # Convert the first letter to uppercase and the rest to lowercase using slicing
    capital_letter = word[0].upper() + word[1:].lower()
else:
    # Keep the word unchanged if it's empty
    capital_letter = word

# Print the final capitalized word
print(f"Capitalized word: {capital_letter}")