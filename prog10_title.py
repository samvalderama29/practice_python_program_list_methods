# Prog10: title() makes all first letter of each word in the string, capital letter. And all other letter in small case.
#         Create a program that do the same functionality without using title() function.

# Get input from the user
print("Make first letter of each word capital without using title()")

# Take input from the user
word = input("Enter a word: ")

# Split the sentence into words based on spaces
split_word = word.split()

# Initialize an empty string to store the final result
title_word = ""

# Iterate through each word in the list
for i in split_word:
    if i: # Check if the word is not empty (to avoid errors)
        title_word += i[0].upper() + i[1:] # Capitalize first letter, keep the rest as is
        title_word += " " # Add a space after each word
    else:
        split_word.index(i) < len(split_word) - 1
        title_word += " " # Preserve spaces

# Print the final sentence with capitalized first letters
print(f"Capitalized first letter word: {title_word}")