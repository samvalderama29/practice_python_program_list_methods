# Prog05: startswith() check if the string beginning part matches the function parameter.
#         Create a program that do the same functionality without using startswith() function.

print("Find the beginning part of the string without using startswith()")

word = input("Enter a word: ")
startword = input("Enter the first letters of the word you input: ")

initial_countword = len(word)
final_countword = len(startword)

equal_word_prefix = word[:final_countword - initial_countword]

if equal_word_prefix == startword:
    print("The words end with the given prefix")
else:
    print("The word does not start with the given prefix")