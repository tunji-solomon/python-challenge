
# ✅ Challenge: Word Frequency from File
# Write a function called word_frequency that:

# 1️⃣ Takes a file path as input.
# 2️⃣ Opens and reads the file line by line.
# 3️⃣ For each line, splits it into words (use spaces only, no .split() if you want to go full manual).
# 4️⃣ For each word:

# Remove any leading/trailing punctuation like ., ,, ?, ! (use your own logic, no strip() if you want the extra challenge!).

# Make it lowercase so it’s case-insensitive.
# 5️⃣ Builds a dictionary mapping each word to the number of times it appears.
# 6️⃣ Returns that dictionary.

# RULES TO FOLLOW
# Don’t use collections.Counter.

# Don’t use .split() or .strip() if you want to push yourself — write your own word splitter and punctuation remover.

# Read line by line — no .read() for the whole file at once.

# Keep your custom get_length or get_index if you like!

#function to split text by given argument and return a new list of splited characters
import os
from most_frequent import get_length

def split_text(text: str, *split_by) -> list:
    new_list = []
    def recursor(text) -> list:
        for i in range(get_length(text)):
            character = text[i]
            if character in split_by:
                new_list.append(text[:i])
                text = text[i + 1:]
                return recursor(text)
        else:
            for i in range(get_length(text)):
                character = text[i]
                if character in ["\n"]:
                    new_list.append(text[:i])                        
            return new_list
        
    return recursor(text)

#Count in number of occurence of words in a list and return a dictionary showing their frequency of occurence
def word_counter(word_list: list[str]) -> dict:
    counter = {}
    for word in word_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            
    return counter  
                
def word_frequency(file_path) -> dict:
    
    
    #function to remove punctuation marks from words
    def punctuation_mark_remover(words_list: list[str]) -> list:
        new_list = [] 
        for word in words_list:
            for i in range(get_length(word)):
                if word[i] in ["!", "?", ",", ".", "-", ":"]:
                    word_modified = word[:i]
                    new_list.append(word_modified)
                    break
            else:
                new_list.append(word)
                    
        return new_list
    
        
    #check if file exist
    if os.path.isfile(file_path) is False:
        return "File does not exist at specified path"
    
    data = None
    all_words_list = []
    #open file and read lines
    with open(file_path) as file:
        data = file.readlines()
    
    #read data line by line
    for line in data:
        #split word by space
        word_after_split = split_text(line, " ")
        #remove punctuation marks from word
        word_without_punctuation = punctuation_mark_remover(word_after_split)
        #add all words from lines into one list
        for word in word_without_punctuation:
            all_words_list.append(word.lower())
            
    # compute frequency of occurence
    frequecy = word_counter(all_words_list)
    
    #just for display sake so i added this, even though the function is meant to return dict.
    # for word, frequecy in frequecy.items():
    #     print(f"{word}: {frequecy}")
        
    #return the frequency
    return frequecy
      

if __name__ == "__main__":
    print(word_frequency("./sample.txt"))
    


        

        
        
        