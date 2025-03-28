# Prog05: endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

print("Math the end part of the string without using endswith()")

word = input("Enter a word: ")
endword = input("Enter the last letters of the word you input: ")

initial_countword = len(word)
final_countword = len(endword)

equal_word_suffix = word[initial_countword - final_countword:]

if equal_word_suffix == endword:
    print("The words end with the given suffix")
else:
    print("The word does not end with the given suffix")