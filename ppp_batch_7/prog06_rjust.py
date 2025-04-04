# Prog06: rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter.
#         Create a program that do the same functionality without using rjust() function.

# Print message that explains the purpose of the program
print("Add space characters without using rjust()")

# Get input from the user
word = input("Enter a word: ")

# Get the desired total length
count_characters = int(input("Enter a number to specify the function parameter: "))

# Check if the word is already as long as or longer than the required length
if len(word) >= count_characters:
    print("Insuffiecient space. Input a bigger number for function parameter")
else:
    complete_word = count_characters - len(word) # Calculate remaining spaces needed
    print(f"String with space characters: {(" " * complete_word) + word}") # Print and add spaces to the word