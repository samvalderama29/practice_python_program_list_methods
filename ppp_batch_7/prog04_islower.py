# Prog04: islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Print message that explains the purpose of the program
print("Check if all characters are on lower case without using islower()")

# Get input from the user
word = input("Enter a word: ")

# Define lowercase letters
lowercase = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

# Variable to track if all characters are lowercase
all_lower = True

# Loop through the string using index positions
for i in range(len(word)): # Using len() to determine string length
    if word[i] not in lowercase: # If a character is not lowercase and not a space
        all_lower = False
        break # Exit loop early for efficiency

# Print the result
if all_lower:
    print("True")
else:
    print("False")