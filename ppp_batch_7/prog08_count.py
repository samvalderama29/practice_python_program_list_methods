# Prog08: count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# Print message that explains the purpose of the program
print("Identify how many times a string appear without using count()")

# Get user input
word = input("Enter a word: ")

# Ask user to input a letter to search for within the word
find_letter = input("Enter a letter you want to find in the word: ")

# Initialize a counter to store the number of occurrences
letter_count = 0

# Iterate through each character in the word
for i in range(len(word)):
    if word[i] == find_letter: # Check if the current character matches the target letter
        letter_count += 1
    else:
        print(f"The letter '{find_letter}' cannot be found in {word}") # Print an error message and break if the letter is not found
    break # This exits the loop immediately after the first unmatched character

# Display the final count of occurrences
print(f"The amount of time '{find_letter}' appear on '{word}': {letter_count}")