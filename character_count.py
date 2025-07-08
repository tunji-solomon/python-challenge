
# ✅ Challenge: Character Frequency Counter
# Write a function called char_frequency that:

# 1️⃣ Takes a single string as input.
# 2️⃣ Counts how many times each character appears in the string.

# Ignore spaces.

# Treat uppercase and lowercase letters as the same (case-insensitive).
# 3️⃣ Returns a dictionary where each key is a character and the value is the count.

def char_frequency(sentence : str) -> dict:
    character_counter = {}
    
    for character in sentence:
        if character == " ":
            continue
        
        character = character.lower()
        if character not in character_counter:
            character_counter[character] = 1
        else:
            character_counter[character] += 1
            
    return character_counter

text = "ProgramMing is fun"

print(char_frequency(text))