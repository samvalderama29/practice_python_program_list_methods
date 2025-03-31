# Prog04: islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

print("Check if all characters are on lower case without using islower()")

word = input("Enter a word: ")

lowercase = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

all_lower = True

for i in range(len(word)):
    if word[i] not in lowercase:
        all_lower = False
        break

if all_lower:
    print("True")
else:
    print("False")