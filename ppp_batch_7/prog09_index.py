# Prog09: index() return the first location of the function parameter in the string.
#         Create a program that do the same functionality without using index() function.

print("Return the first location of the string without using index()")

word = input("Enter a word: ")

find_letter = input("Enter a letter you want to find")

word_position = -1

for i in range(len(word)):
    if word[i] == find_letter:
        position = i
        break