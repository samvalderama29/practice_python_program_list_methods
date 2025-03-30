# Prog03: upper() converts all characters of the string into upper case.
#         Create a program that do the same functionality without using upper() function.

# Print message that explains the purpose of the program
print("Convert all characters of the string into upper case without using upper()")

# Get input from the user
word = input("Enter a word: ")

# Create variable to store uppercase and lowercase letters
uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
lowercase = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

# Replace each lowercase letter with its lowercase equivalent
for i in range(len(uppercase)):
    word = word.replace(lowercase[i], uppercase[i])

# Print the final in lowercase string
print(f"String in uppercase: {word}")