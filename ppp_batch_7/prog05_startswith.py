# Prog05: startswith() check if the string beginning part matches the function parameter.
#         Create a program that do the same functionality without using startswith() function.

# Print message that explains the purpose of the program
print("Find the beginning part of the string without using startswith()")

# Get input from the user
word = input("Enter a word: ")
startword = input("Enter the first letters of the word you input: ")

# Get the length of the word and prefix
initial_countword = len(word)
final_countword = len(startword)

# Extract the last part of the word manually
equal_word_prefix = word[:final_countword - initial_countword]

# Compare manually
if equal_word_prefix == startword:
    print("The words end with the given prefix")
else:
    print("The word does not start with the given prefix")