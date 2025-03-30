# Prog01: lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Print message that explains the purpose of the program
print("Remove space characters at the beginning of the string without using lstrip()")

# Taking user input with spaces or tabs at the beginning
word = input("Enter a word (include spaces at the beginning): ")

# Variable to track the position of the first non-space character
space = 0

# Loop through the string until a non-space and non-tab character is found
while space < len(word) and word[space] in (" ", "\t"):
    space += 1

# Slice the string from the first non-space character
removespace = word[space:]

# Display the result without leading space
print(f"String without leading spaces: {removespace}")