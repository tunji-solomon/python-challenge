# ✅ Challenge: Word Length Categorizer
# Write a function called categorize_words that:

# 1️⃣ Accepts a list of words (strings).
# 2️⃣ For each word, determine its length.
# 3️⃣ Return a dictionary that groups the words by their lengths.

# The key is the word length (an integer).

# The value is a list of all words with that length.

def categorize_word(word_list: list[str]) -> dict:
    
    word_length_counter = {}
    
    def counter(word: str) -> int: #I defined this function to subtitute for the built in
        count = 0
        for _ in word:
            count += 1
        return count
            

    for word in word_list:
        word_length = counter(word)
        if word_length not in word_length_counter:
            word_length_counter[word_length] = [word]
        else:
            word_length_counter[word_length].append(word)
            
    return word_length_counter
            
words = ["cat", "hello", "hi", "world", "Python", "go"]

print(categorize_word(words))
        