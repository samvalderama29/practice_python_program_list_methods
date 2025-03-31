# Prog07: zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter.
#         Create a program that do the same functionality without using zfill() function.

print("Add zero without using zfill()")

user_number = (input("Enter a number: "))

user_number_count = int(input("Enter a number to specify the function parameter: "))

if len(user_number) >= user_number_count:
    print("Insufficient space. Input a bigger number for function parameter")
else:
    complete_zero = user_number_count - len(user_number)
    print(f"String filled with zero characters: {("0" * complete_zero) + user_number}")