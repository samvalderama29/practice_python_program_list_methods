# Prog02: removesuffix() remove the characters at the end of the string that matches the function parameter.
#         Create a program that do the same functionality without using removesuffix() function.

# Print message that explains the purpose of the program
print("Remove the characters at the end of the string without using removesuffix()")

# Get input string from the user
word = input("Enter a word: ")

# Ask the user what suffix to remove
suffixword = input("Enter the suffix you want to remove from the string: ")

# Calculate the length of the word and the suffix
word_count = len(word)
suffixword_count = len(suffixword)

# Check if the word ends with the given suffix
if word[word_count - suffixword_count:] == suffixword:
    finalword = word[:word_count - suffixword_count] # Remove the suffix using slicing
    print(f"String after suffix removal: {finalword}") # Print final result
else:
    print("Invalid suffix. The suffix you input cannot be found in the end of the word. Try again.")