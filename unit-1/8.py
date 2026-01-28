# 8. Write a Python program to perform following operation on given string
# input:
# a) Count Number of Vowel in given string
# b) Count Length of string (donot use len() )
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not

# Input from user
text = input("Enter a string: ")

# Define vowels (both cases)
vowels = "aeiouAEIOU"

# Count vowels using a loop
count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels in the given string: {count}")

# Input from user
text = input("Enter a string: ")

# b) Count Length of string (without using len())
length = 0
for char in text:
    length += 1

# c) Reverse string
# Using slicing [start:stop:step]. -1 step moves backwards.
reversed_text = text[::-1]

# d) Find and replace operation
search_word = input("Enter the character/substring to find: ")
replace_word = input("Enter the replacement: ")
# We can use the built-in .replace() method for this specific operation
replaced_text = text.replace(search_word, replace_word)

# e) Check whether string entered is a palindrome or not
# A palindrome reads the same forward and backward (e.g., "radar")
# We use .lower() to ensure the check isn't case-sensitive
is_palindrome = text.lower() == reversed_text.lower()

# --- Output Results ---
print("-" * 20)
print(f"Length of string: {length}")
print(f"Reversed string: {reversed_text}")
print(f"After replacement: {replaced_text}")
print(f"Is Palindrome? {'Yes' if is_palindrome else 'No'}")