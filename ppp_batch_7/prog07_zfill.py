# Prog07: zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter.
#         Create a program that do the same functionality without using zfill() function.

# Print message that explains the purpose of the program
print("Add zero without using zfill()")

# Get input from the user
user_number = (input("Enter a number: "))

# Get the desired total length
user_number_count = int(input("Enter a number to specify the function parameter: "))

# Check if the word is already as long as or longer than the required length
if len(user_number) >= user_number_count:
    print("Insufficient space. Input a bigger number for function parameter")
else:
    complete_zero = user_number_count - len(user_number) # Calculate remaining zero needed
    print(f"String filled with zero characters: {("0" * complete_zero) + user_number}") # Print and add zeros to the word