# What is a String?
# A string is a group of characters.
# Strings are written inside single (' ') or double (" ") quotes.
# Example: 'Hello', "Python".

# Task 1: Repeat the word "Hello" 5 times.
# Task 2: Print the length of the word "Computer".
# Task 3: Print the first letter of your school name using an index.


# Creating a String
name = "Riya"
print(name)

# String Repetition - Using * to repeat a string

word = "Hi "
print(word * 3)

# Finding Length of a String -len() gives the number of characters in a string.

text = "Python"
print(len(text))

# Accessing Characters using Index - Index starts from 0 and ends with n-1.

subject = "Coding"
print(subject[0])   # First character
print(subject[3])   # Fourth character


# Looping through a String
for letter in "CAT":
    print(letter)

# Changing Case of String
message = "hello"
print(message.upper())   # Converts to CAPITAL letters
print(message.lower())   # Converts to small letters
