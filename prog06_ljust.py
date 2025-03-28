# Prog06: ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

print("Add space characters without using ljust()")

word = input("Enter a word: ")

count_characters = int(input("Enter a number to specify the function parameter: "))

if len(word) >= count_characters:
    print("Insuffiecient space. Input a bigger number for function parameter")
else:
    complete_word = count_characters - len(word)
    print(f"String with space characters: {word + (" " * complete_word)}")