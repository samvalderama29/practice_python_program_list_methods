# Prog08: swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Print message that explains the purpose of the program
print("Reverse the casing of each of the character of the string without using swapcase()")

# Get user input
word = input("Enter a word: ")

# Define uppercase and lowercase letters as strings
uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
lowercase = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

# Initialize an empty string to store the swapped case word
swap_word = ""

# Loop through each character in the input word
for i in range(len(word)):
    if word[i] in uppercase:
        #  Find the index of the uppercase letter and replace it with the corresponding lowercase letter
        count_upper = uppercase.index(word[i])
        swap_word += lowercase[count_upper]
    elif word[i] in lowercase:
        # Find the index of the lowercase letter and replace it with the corresponding uppercase letter
        count_lower = lowercase.index(word[i])
        swap_word += uppercase[count_lower]
    else:
        # Keep space characters unchanged
        swap_word += word[i]

# Print the final swapped case word
print(f"Swapped case word: {swap_word}")