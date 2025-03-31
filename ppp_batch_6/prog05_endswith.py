# Prog05: endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Print message that explains the purpose of the program
print("Find the end part of the string without using endswith()")

# Get input from the user
word = input("Enter a word: ")
endword = input("Enter the last letters of the word you input: ")

# Get the length of the word and suffix
initial_countword = len(word)
final_countword = len(endword)

# Extract the last part of the word manually
equal_word_suffix = word[initial_countword - final_countword:]

# Compare manually
if equal_word_suffix == endword:
    print("The words end with the given suffix")
else:
    print("The word does not end with the given suffix")