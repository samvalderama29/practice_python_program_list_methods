# Prog10: rindex() return the first location of the function parameter in the string starting from the last character.
#         Create a program that do the same functionality without using rindex() function.

# Print message that explains the purpose of the program
print("Find the last occurrence in a string without using rindex()")

# Get user input
word = input("Enter a word: ")

# Ask user to input a letter to search for within the word
find_letter = input("Enter a letter you want to find: ")

# Initialize a variable to track position
word_position = -1 # Default to -1 if the character is not found

# Iterate through the string in reverse order to find the last occurrence
for i in range(len(word) -1, -1, -1): # Start from the last index and move backward
    if word[i] == find_letter:
        word_position = i  # Store the first matching index from the end
        break # Stop the loop after finding the last occurrence

# Display the result
if word_position != -1:
    print(f"The last occurrence of '{find_letter}' is at index {word_position}")
else:
    print(f"The letter '{find_letter}' was not found in '{word}'")