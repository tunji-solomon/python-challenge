# ✅ Challenge: Vowel Counter Dictionary
# Write a function called count_vowels that:
# 1️⃣ Takes a list of words (strings).
# 2️⃣ For each word, counts the number of vowels (a, e, i, o, u) — case-insensitive.
# 3️⃣ Returns a dictionary where each key is the word and each value is its vowel count.

#Note: I intentionally used arbitary positional argument cause i needed to try something different

def count_vowels(*words) -> dict:
    
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = {}
    
    for word in words:
        vowel_counter[word] = 0
        for character in word.strip().lower():
            if character in vowels:
                vowel_counter[word] += 1
                
    return vowel_counter

print(count_vowels("Apple", "banAna", "OrangE", "sky"))
                
                
                