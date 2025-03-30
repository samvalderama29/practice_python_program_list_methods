# Prog02: removesuffix() remove the characters at the end of the string that matches the function parameter.
#         Create a program that do the same functionality without using removesuffix() function.

print("Remove the characters at the end of the string without using removesuffix()")

word = input("Enter a word: ")

suffixword = input("Enter the suffix you want to remove from the string: ")

word_length = word.strip(suffixword)

if word_length in word:
    finalword = word.rstrip(suffixword)
    print(f"String after suffix removal: {finalword}")
else:
    print("Invalid suffix. The suffix you input cannot be found in the word. Try again.")