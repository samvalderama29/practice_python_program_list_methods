# Prog02: removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

print("Remove characters at the beginning of the string without using removeprefix()")

word = input("Enter a word: ")

prefixword = input("Enter the prefix you want to remove from the string: ")

finalword = word.strip(prefixword)

print(finalword)