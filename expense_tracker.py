
# 🎯 Project Goal
# Build a command-line expense tracker that:

# Reads a simple CSV (or .txt) file containing your daily expenses.

# Summarizes your spending by category and date.

# Outputs a summary file with totals and basic stats.

# You do everything with your own string parsing — no csv module, no pandas.

# ✅ Your Tracker Must Do
# 1️⃣ Read the file line by line.
# 2️⃣ Split each line into:

# Date

# Category

# Amount (float)

# Note/description
# 3️⃣ Validate each line (skip lines with missing or invalid data).
# 4️⃣ Sum totals by category (e.g., Food: $32.50, Transport: $8.00, Entertainment: $15.00).
# 5️⃣ Sum totals by date.
# 6️⃣ Write a summary file like expenses_summary.txt:
    
# ✅ Rules
# Don’t use csv or pandas — do your own splitting with your custom helpers.

# Use your own get_length, get_index, or split_text functions.

# Validate Amount — it must be a number.

# Skip or handle any bad lines gracefully.

# 🏅 Your deliverable
# A single Python file that:

# Reads the raw file.

# Produces the summary file.

# Uses your custom parsing logic.

# Prints "Summary written to expenses_summary.txt" when done.

def expense_tracker(source_file, output_file) -> None:
    import os
    from file_word_freq import split_text
    
    if os.path.isfile(source_file) is False:
        print("File not found at specified path")
        return
    data = None
    with open(source_file) as file:
        data = file.readlines()
    expenses_by_date = []
    expenses_by_category = []
    category_expense_summary = {}
    date_expense_summary = {}
    for line in data:
        splitted_line = split_text(line, ",")
        if len(splitted_line) != 4:
            continue

        expenses_by_date.append((splitted_line[0], float(splitted_line[2])))
        expenses_by_category.append((splitted_line[1], float(splitted_line[2])))

    for data in expenses_by_category:
        if data[0] in category_expense_summary:
            category_expense_summary[data[0]] += data[1]
        else:
            category_expense_summary[data[0]] = data[1]
            
    for data in expenses_by_date:
        if data[0] in date_expense_summary:
            date_expense_summary[data[0]] += round(data[1], 2)
        else:
            date_expense_summary[data[0]] = round(data[1], 2)
            
    total_expenses = 0
    for exp in category_expense_summary.values():
        total_expenses += exp
        
    with open(output_file, "+a") as file:
        file.write(f"Total spent: ${total_expenses:.2f}\n")
        file.write("\n")
        
        file.write("By category:\n")
        for category, exp in category_expense_summary.items():
            file.write(f"{category}: ${exp:.2f}\n")
        file.write("\n")
        
        file.write("By date:\n")
        for date, exp in date_expense_summary.items():
            file.write(f"{date}: ${exp:.2f}\n")
        file.write("\n")
                       

if __name__ == "__main__":
    expense_tracker("expense.txt", "expense_summary.txt")
    