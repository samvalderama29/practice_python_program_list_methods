# Prog05: startswith() check if the string beginning part matches the function parameter.
#         Create a program that do the same functionality without using startswith() function.

print("Find the beginning part of the string without using startswith()")

word = input("Enter a word: ")
endword = input("Enter the last letters of the word you input: ")

initial_countword = len(word)
final_countword = len(endword)

equal_word_prefix = word[:final_countword - initial_countword]

if equal_word_prefix == endword:
    print("The words end with the given prefix")
else:
    print("The word does not start with the given prefix")