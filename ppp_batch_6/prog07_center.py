# Prog07: center() add space characters at the beginning and at the end of the string to print the string at the center.
#         Create a program that do the same functionality without using center() function.

# Print message that explains the purpose of the program
print("Add space at the beginning and end of the string without using center()")

# Get user input for the word
word = input("Enter a word: ")

# Get user input for the total width of the centered string
count_space = int(input("Enter a number: "))

# Check if the word is too long to be centered within the given width
if len(word) >= count_space:
    print("Invalid. The word is too long to be centered")
else:
    total_spaces = count_space - len(word) # Calculate the total number of spaces needed
    left_spaces = total_spaces // 2 # Divide the spaces equally, placing half on the left
    centered_word = word.rjust(len(word) + left_spaces).ljust(count_space) # Use rjust to add left spaces, then ljust to add right spaces
    print(f"Centered string: '{centered_word}'") # Print the final centered word with spaces