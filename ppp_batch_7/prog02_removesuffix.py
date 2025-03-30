# Prog02: removesuffix() remove the characters at the end of the string that matches the function parameter.
#         Create a program that do the same functionality without using removesuffix() function.

print("Remove the characters at the end of the string without using removesuffix()")

word = input("Enter a word: ")

suffixword = input("Enter the suffix you want to remove from the string: ")

word_count = len(word)
suffixword_count = len(suffixword)

if word[word_count - suffixword_count:] == suffixword:
    finalword = word[:word_count - suffixword_count]
    print(f"String after suffix removal: {finalword}")
else:
    print("Invalid suffix. The suffix you input cannot be found in the end of the word. Try again.")