
# ✅ Challenge: Word Counter from a File
# Write a function called count_words_in_file that:

# 1️⃣ Takes a file path as input.
# 2️⃣ Opens the file and reads its content line by line.
# 3️⃣ For each line, split it into words (you can split on spaces only).
# 4️⃣ Count the total number of words in the whole file.
# 5️⃣ Return that count.

def count_words_in_file(filepath: str) -> int | str:
    import os
    
    #function to get length of an iterable just like built in len function
    def get_length(iterable) -> int:
        length = 0
        for _ in iterable:
            length += 1
        return length
    
    
    #function to get the index of the first occurence of an item in an iterable
    def get_index(item, iterable) -> int | None:
        index = 0
        while index < get_length(iterable):
            if iterable[index] == item:
                return index
            index += 1
        else:
            return None
    
    data = None
    #check if file path exist
    if os.path.isfile(filepath) is True:
        with open(filepath, "r") as file:
            data = file.readlines()
    else: 
        return "File path does not exist, PLease create file in specified path or try a diffrent file"
    
            
    #count words retrieved from file line by line
    word_count = 0  
    # letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for line in data:
        for character in line:
            if character == " " or character == "\n" or get_index(character, line) == get_length(line) - 1:
                word_count += 1
                line = line[get_index(character, line) + 1:]
            
            # if character not in letters:
            #     word_count += 1
            
    return word_count
        
            
print(count_words_in_file("./sample.txt"))
    