# Prog08: count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

print("Identify how many times a string appear without using count()")

word = input("Enter a word: ")

find_letter = input("Enter a letter you want to find in the word: ")

letter_count = 0

for i in range(len(word)):
    if word[i] == find_letter:
        letter_count += 1
    else:
        print(f"The letter '{find_letter}' cannot be found in {word}")
    break

print(f"The amount of time '{find_letter}' appear on '{word}': {letter_count}")