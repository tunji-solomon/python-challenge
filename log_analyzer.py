# ✅ Challenge: Log File Analyzer
# Function name: analyze_log

# 📌 What it must do
# 1️⃣ Takes one input — a log file path (e.g., "logs.txt").

# 2️⃣ Reads the log file line by line.

# 3️⃣ For each line, extract:

# The log level (e.g., INFO, ERROR, WARNING).

# The date in format YYYY-MM-DD.

# 4️⃣ Builds and returns a summary dictionary:

# Each log level should be a key with the count of its occurrences.

# Include a nested key called "dates" which is another dictionary counting how many total logs exist for each date.

# 5️⃣ Return the final summary dictionary.

# ✅ Rules
# Do not use regex or any special log libraries.

# Use your own custom string parsing and counting logic.

# Handle missing files by returning a clear message like "File does not exist".

# If a line doesn’t match the expected pattern, skip it safely.

def analyze_log(filepath) -> dict:
    import os
    from most_frequent import get_length
    from file_word_freq import split_text, word_counter
    
    if os.path.isfile(filepath) is False:
        print("File not available at specified path")
        return
    data = None
    with open(filepath, "r") as file:
        data = file.readlines()
        
    log_level_list = []
    log_date_list = []
    
    for line in data:
        log_message = ''
        splitted_log = split_text(line, " ")
        
        for i in range(3, get_length(splitted_log)):
            if i == 3:
                log_message += f"{splitted_log[i]}"
            else:
                log_message += f" {splitted_log[i]}"
                
        splitted_log[3:] = [log_message]
            
        if get_length(splitted_log) < 4:
            continue
        if splitted_log[0][0] != "[" and "]" in splitted_log == False:
            continue
        log_level_list.append(splitted_log[0])
        log_date_list.append(splitted_log[1])
    
    level_list = []
    for log_level in log_level_list:
        log_level = log_level[1:-1]
        level_list.append(log_level)
        
    log_summary = word_counter(level_list) 
    log_summary["Date"] = {}
    
    date_counter = word_counter(log_date_list)
    
    for key, value in date_counter.items():
        log_summary["Date"][key] = value
    
    return log_summary
        
print(analyze_log("logs.txt"))
        
    
    