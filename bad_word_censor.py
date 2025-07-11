
# ✅ Challenge: Censor Bad Words in a File
# Write a function called censor_file that:

# 1️⃣ Takes two file paths as input:

# The source file (a .txt file with lines of text).

# The output file where you’ll save the censored text.

# 2️⃣ Reads the source file line by line.

# 3️⃣ Has a list of banned words (e.g., ["bad", "ugly"]).

# 4️⃣ For each banned word in each line:

# Replace the banned word with *** (exact match only, case-insensitive).

# Do this manually — no .replace() allowed!

# You can write your own helper to do the replacement character by character.

# 5️⃣ Write the censored lines to the output file.

# 💡 Rules
# Don’t use .replace().

# You can use your own split or index helpers.

# Write the censored lines back to the file line by line.

# Preserve punctuation and spaces around the censored words.

def censor_file(source_file, output_file) -> None:
    import os
    from most_frequent import get_length
    from file_word_freq import split_text
    
    def censor_word(word_list: list[str], *words_to_censor) -> list:
        
        for i in range(get_length(word_list)):
            word = word_list[i]
            punctuation = ""
            word_without_punctuation = ""
            
            for j in range(get_length(word)):
                if  word[j] in ".!-?, ":
                    punctuation += word[j]
                else:
                    word_without_punctuation += word[j]
                    
            if word_without_punctuation.lower() in words_to_censor:
                word_list[i] = "*"*get_length(word_without_punctuation) + punctuation
                
        return word_list
                
    if os.path.isfile(source_file) is False:
        return "Specified source file does not exist"
    
    data = None
    with open(source_file) as file:
        data = file.readlines()
    import time
    for line in data:
        sentence_splitted = split_text(line, " ")
        censored_words_list = censor_word(sentence_splitted, "bad", "ugly")
        with open(f"./{output_file}", "+a") as file:
            for word in censored_words_list:
                time.sleep(0.5)
                file.write(f"{word} ")
            file.write("\n")
    
                
    print(f"File censored successfully and outputed to {output_file}")
            
censor_file("sample.txt", "censored.txt")
    
    