# Prog05: endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

print("Math the end part of the string without using endswith()")

word = input("Enter a word: ")

endword = input("Enter the last letters of the word you input: ")

initial_countword = len(word)

final_countword = len(endword)

if initial_countword.index() == final_countword: