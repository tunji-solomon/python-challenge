# ✅ Next Step: Add New Expenses Interactively
# 🎯 What you’ll add
# Extend your expense_tracker project so you can:
# 1️⃣ Run the script in a “Add Mode”, where the user enters:

# Date (YYYY-MM-DD)

# Category

# Amount

# Description

# 2️⃣ Each new expense gets appended to your expenses.txt file in the same format:
# 3️⃣ When done, you can run the summary again to update totals.

# ✅ How it should work
# Prompt the user for each field, one by one.

# Validate:

# The amount is a valid float.

# The date looks like YYYY-MM-DD (basic check — just for practice).

# Append the new line to your source file — no overwriting!

# Confirm success: "Expense added!"

# ✨ How to structure it
# You can either:
# ✅ Write a new function, e.g., add_expense(),
# ✅ Or wrap both the expense_tracker() and add_expense() in a simple main() that asks if the user wants to “Add” or “Summarize”.

from expense_tracker import expense_tracker
from most_frequent import get_length
import os

def expense_management_app(expense_file) -> None:
    
    def remove_trailing_space(string: str) -> str:
        new_string = ""
        for i in range(get_length(string)):
            if string[i] != " ":
                break
            else:
                new_string = string[i + 1:]        
                string = new_string
        for i in range(1, get_length(new_string)):
            if new_string[-i] != " ":
                break
            else:
                string = new_string[0:-i]
                
        return string
    def amount_validator(string : str) -> bool:
        if len(string) < 1:
            return False
        if string[0] == "." or string[-1] == ".":
            return False
        if "." not in string:
            return False
        for i in range(get_length(string)):
            if string[i] in ".0123456789" == False:
                return False
            if string[i] == ".":
                print(i, "and", get_length(string)-i)
                if not get_length(string) - i == 3:
                    return False
        else:
            return True

        
    
    def date_validator(date : str) -> bool:
        if get_length(date) != 10:
            return False
        if date[4] != "-" or date[7] != "-":
                return False
        for i in range(get_length(date)):
            if i == 4 or i == 7:
                continue
            if date[i] in "0123456789" == False:
                return False
        else:
            return True   

    print("Welcome to expense management application......\n")
    while True:

        print("Menu")
        print("="*4)
        
        menu_list = ["Add expense", "Summarize expense", "Exit application"]
        
        for i in range(get_length(menu_list)):
            print(f"Enter {i + 1} to {menu_list[i]}\n")
            
        option_selected = remove_trailing_space(input("Enter your option here: "))
        if option_selected == "1":
            while True:
                date = remove_trailing_space(input("\nEnter date expenses was incured: "))
                if date_validator(date) == True:
                    break
                else:
                    print("\nDate must be of format -> YYYY-MM-DD. Please provide a valid format")
            category = remove_trailing_space(input("\nEnter the category of expenses: "))
            while True:
                amount = remove_trailing_space(input("\nEnter the amount spent: $"))
                if amount_validator(amount) == True:
                    break
                else:
                    print("\nAmount must be of type float. example: $50.00")
            description = remove_trailing_space(input("\nEnter description of expenses: "))
            
            if os.path.isfile(expense_file) is False:
                return "\nFile does not exist at specified path"
            
            with open(expense_file, "+a") as file:
                file.write(f"{date},{category},{amount},{description}\n")
                
            print(f"\nExpense added to {expense_file}")
            
            
        if option_selected == "2":
            summary_file = "expense_summary.txt"
            expense_tracker(expense_file,summary_file)
            
        if option_selected == "3":
            print("\nYou exited the application")
            break
    
    
    
expense_management_app("expense.txt")
    

