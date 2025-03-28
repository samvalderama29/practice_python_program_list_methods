# Prog07: center() add space characters at the beginning and at the end of the string to print the string at the center.
#         Create a program that do the same functionality without using center() function.

print("Add space at the beginning and end of the string without using center()")

word = input("Enter a word: ")

count_space = int(input("Enter a number: "))

if len(word) >= count_space:
    print("Invalid. The word is too long to be centered")
else:
    total_spaces = count_space - len(word)
    left_spaces = total_spaces // 2
    centered_word = word.rjust(len(word) + left_spaces).ljust(count_space)
    print(f"Centered string: '{centered_word}'")