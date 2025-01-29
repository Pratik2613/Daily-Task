### 1. Count letters, digits, and special symbols in a string

def count_elements(s):
    chars = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    symbols = sum(not c.isalnum() for c in s)
    
    print(f"Chars = {chars}")
    print(f"Digits = {digits}")
    print(f"Symbol = {symbols}")

input_str = "P@#yn26at^&i5ve"
count_elements(input_str)


### 2. Remove duplicate characters from a string

def remove_duplicates(s):
    words = s.split()
    seen = set()
    result = []
    
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return " ".join(result)

input_str = "String and String Function"
output_str = remove_duplicates(input_str)
print(output_str)


### 3. Count uppercase, lowercase, numbers, and special characters in a string

def count_character_types(s):
    upper_case = sum(c.isupper() for c in s)
    lower_case = sum(c.islower() for c in s)
    numbers = sum(c.isdigit() for c in s)
    special_case = sum(not c.isalnum() and not c.isspace() for c in s)

    print(f"UpperCase : {upper_case}")
    print(f"LowerCase : {lower_case}")
    print(f"NumberCase : {numbers}")
    print(f"SpecialCase : {special_case}")

input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
count_character_types(input_str)


### 4. Count vowels in a string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for c in s if c in vowels)
    print(f"Total vowels are: {count}")

input_str = "Welcome to Python Assignment"
count_vowels(input_str)
```

These programs efficiently solve each of your problems. Let me know if you need modifications! 🚀
