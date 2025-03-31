# Prog07: zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter.
#         Create a program that do the same functionality without using zfill() function.

print("Add zero without using zfill()")

user_number = (input("Enter a number: "))

user_number_count = (input("Enter a number to specify the function parameter: "))

user_number_length = len(user_number)
user_number_count_length = len(user_number_count)

final_zero = user_number_length - user_number_count_length

if user_number_count_length >= user_number_length:
    print("Insufficient space. Input a bigger number for function parameter")
else:
    print(f"{(final_zero * "0") + user_number}")