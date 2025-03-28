# Prog04: isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Print message that explains the purpose of the program
print("Check if all characters are on upper case without using isupper")

# Get input from the user
word = input("Enter a word: ")

# Define uppercase letters
uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "

# Variable to track if all characters are uppercase
all_upper = True

# Loop through the string using index positions
for i in range(len(word)): # Using len() to determine string length
    if word[i] not in uppercase: # If a character is not uppercase and not a space
        all_upper = False
        break # Exit loop early for efficiency

# Print the result
if all_upper:
    print("True")
else:
    print("False")