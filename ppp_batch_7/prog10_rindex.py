# Prog10: rindex() return the first location of the function parameter in the string starting from the last character.
#         Create a program that do the same functionality without using rindex() function.

print("Find the last occurrence in a string without using rindex()")

word = input("Enter a word: ")

find_letter = input("Enter a letter you want to find: ")

word_position = -1

for i in range(len(word) -1, -1, -1):
    if word[i] == find_letter:
        word_position = i
        break

# Display the result
if word_position != -1:
    print(f"The last occurrence of '{find_letter}' is at index {word_position}")
else:
    print(f"The letter '{find_letter}' was not found in '{word}'")