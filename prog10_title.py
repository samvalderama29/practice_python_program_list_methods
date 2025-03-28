# Prog10: title() makes all first letter of each word in the string, capital letter. And all other letter in small case.
#         Create a program that do the same functionality without using title() function.

print("Make first letter of each word capital without using title()")

word = input("Enter a word: ")

split_word = word.split()

title_word = ""

for i in split_word:
    if i:
        title_word += i[0].upper() + i[1:]
        title_word += " "
    else:
        split_word.index(i) < len(split_word) - 1
        title_word += " "

print(f"Capitalized first letter word: {title_word}")