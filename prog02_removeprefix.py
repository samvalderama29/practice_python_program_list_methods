# Prog02: removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# Print message that explains the purpose of the program
print("Remove characters at the beginning of the string without using removeprefix()")

# Get input string from the user
word = input("Enter a word: ")

# Ask the user what prefix to remove
prefixword = input("Enter the prefix you want to remove from the string: ")

# Attempt to remove the prefix using strip() (Note: strip() removes characters, not a full prefix)
finalword = word.strip(prefixword)

# Print the final result
print(finalword)