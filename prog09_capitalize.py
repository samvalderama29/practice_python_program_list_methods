# Prog09: capitalize() makes the first letter of the string, capital letter. And all other letter in small case.
#         Create a program that do the same functionality without using capitalize() function.

print("Make the first letter capital without using capitalize()")

word = input("Enter a word: ")

if word:
    capital_letter = word[0].upper() + word[1:].lower()
else:
    capital_letter = word

print(f"Capitalized word: {capital_letter}")