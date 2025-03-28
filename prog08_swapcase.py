# Prog08: swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

print("Reverse the casing of each of the character of the string without using swapcase()")

word = input("Enter a word: ")

uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
lowercase = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

swap_word = ""

for i in range(len(word)):
    if word[i] in uppercase:
        count_upper = uppercase.index(word[i])
        swap_word += lowercase[count_upper]
    elif word[i] in lowercase:
        count_lower = lowercase.index(word[i])
        swap_word += uppercase[count_lower]
    else:
        swap_word += word[i]

print(f"Swapped case word: {swap_word}")