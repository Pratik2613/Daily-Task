#1. Write a Python program to count the occurrences of each word in a given sentence

string = "To change the overall look of your document. To change the look available in the gallery"
# Convert string to lowercase and split it into words
words = string.lower().split()
# Create a dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    word = word.strip(".")  # Remove punctuation (if any)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word count
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2. Write a Python program to remove a newline in Python

string = "\nBest \nDeeptech \nPython \nTraining\n"
# Remove leading and trailing newlines using strip()
clean_string = string.strip()
print("String without newlines:")
print(clean_string)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3. Write a Python program to reverse words in a string

string = "Deeptech Python Training"
# Split the string into words
words = string.split()
# Reverse the list of words
reversed_words = words[::-1]
# Join them back into a string
reversed_string = " ".join(reversed_words)
print("Reversed string:")
print(reversed_string)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#4. Write a Python program to count and display the vowels of a given text
string = "Welcome to python Training"
vowels = "aeiouAEIOU"
vowel_count = 0
vowel_chars = ""

# Loop through each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1
        vowel_chars += char  # Concatenate vowel characters

print(f"Vowels count: {vowel_count}")
print(f"Vowel characters: {vowel_chars}")
