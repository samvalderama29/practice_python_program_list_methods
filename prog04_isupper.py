# Prog04: isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

print("Check if all characters are on upper case without using isupper")

word = input("Enter a word: ")

uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "

all_upper = True

for i in range(len(word)):
    if word[i] not in uppercase:
        all_upper = False
        break

if all_upper:
    print("All words are in upper case format")
else:
    print("Input is incorrect! Characters must be all in capital letter")