# Prog01: rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

print("Remove space at the end of the string without using rstrip()")

word = input("Enter a word (include spaces at the end): ")

space = 0

while space < len(word) and word[space] in (" ", "\t"):
    space =+ 1

removespace = word[:space]

print(f"String without ending spaces: {removespace})