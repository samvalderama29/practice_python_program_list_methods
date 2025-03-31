# Prog09: index() return the first location of the function parameter in the string.
#         Create a program that do the same functionality without using index() function.

# Print message that explains the purpose of the program
print("Return the first location of the string without using index()")

# Get user input
word = input("Enter a word: ")

# Ask user to input a letter to search for within the word
find_letter = input("Enter a letter you want to find: ")

# Initialize a variable to track position
word_position = -1 # Default to -1 if the character is not found

# Iterate through the string to find the first occurrence
for i in range(len(word)):
    if word[i] == find_letter:
        word_position = i # Store the first found position
        break # Exit loop after finding the first occurrence

# Display the result
if word_position != -1:
    print(f"The first occurrence of '{find_letter}' is at index {word_position}")
else:
    print(f"The letter '{find_letter}' was not found in '{word}'")