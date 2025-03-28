# Prog01: lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

print("Remove space characters at the beginning of the string without using lstrip()")

word = input("Enter a word (include spaces at the beginning): ")

space = 0

while space < len(word) and word[space] in (" ", "\t"):
    space += 1

removespace = word[space:]

print(f"String without leading spaces: {removespace}")