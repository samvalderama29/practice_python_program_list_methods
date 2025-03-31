# Prog09: index() return the first location of the function parameter in the string.
#         Create a program that do the same functionality without using index() function.

print("Return the first location of the string without using index()")

word = input("Enter a word: ")

find_letter = input("Enter a letter you want to find: ")

word_position = -1

for i in range(len(word)):
    if word[i] == find_letter:
        word_position = i
        break

if word_position != -1:
    print(f"The first occurrence of '{find_letter}' is at index {word_position}")
else:
    print(f"The letter '{find_letter}' was not found in '{word}'")