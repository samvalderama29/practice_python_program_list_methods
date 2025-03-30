# Prog01: rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Print message that explains the purpose of the program
print("Remove space at the end of the string without using rstrip()")

# Taking user input with spaces or tabs at the end
word = input("Enter a word (include spaces at the end): ")

# Start from the last character index
space = len(word) - 1

# Move backwards while the character is a space or tab
while space >= 0 and word[space] in (" ", "\t"):
    space =- 1

# Slice the string to exclude end spaces
removespace = word[:space + 1]

# Display the result without end spaces
print(f"String without ending spaces: '{removespace}'")