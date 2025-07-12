# ✅ Tiny Auth System — Project Spec
# 🎯 Goal
# Build a simple command-line app that lets you:
# 1️⃣ Register new users with username + password
# 2️⃣ Store users securely in a plain .txt file (one line per user)
# 3️⃣ Log in as an existing user
# 4️⃣ Lock out any user after 3 failed login attempts
# 5️⃣ Use your own logic for “hashing” the password (optional, but you can do a simple letter shift or number mask) — no hashlib or built-ins

# ✅ Basic rules
# No fancy built-in hashlib or security libraries — you’ll do a simple “pseudo-hash” with your own code.

# Use your get_length, split_text, or any helpers you want — your style!

# Validate input — e.g., no duplicate usernames, no empty fields.

# Keep user data in a file called users.txt:

#Each login attempt must check the file and match the stored “hashed” password.

# 📌 How it works
# 1️⃣ On startup, show a menu:
# 1) Register new user
# 2) Login
# 3) Exit
# 2️⃣ If registering:

# Prompt for username + password

# Check for duplicates — no two users can have the same username.

# Store the username and pseudo-hashed password on a new line.

# 3️⃣ If logging in:

# Prompt for username + password.

# Hash the input password the same way.

# Compare to the file.

# Allow only 3 failed attempts — then exit login mode for that user.

# 4️⃣ If exit:

# Cleanly exit the app.

# 🟢 Bonus: Simple pseudo-hash
# If you want to do a “pure logic” pseudo-hash:

# Take each letter’s Unicode code, add +1 to it, and rebuild the string.

# For numbers, shift each digit by +1 (e.g., 1 → 2).

# This keeps the passwords “unreadable” at a glance.

# 🏅 Deliverable
# A single Python file that:

# Runs in the terminal.

# Stores users.txt in the same folder.

# Uses only your custom helpers.

# Handles input, validation, and error cases robustly.
import os
from custom_split import split
from most_frequent import get_length
import random

characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.#%&*@!$?"

def generate_random(length : int) -> str:
    
    random_generated = ""
    characters_length = get_length(characters)
    for _ in range(length):
        random_generated += characters[random.randint(0,characters_length - 1)]
        
    return random_generated
        
class HashPass:
    
    encryption = {}
    encryption_folder = "./data_files/"
    encryption_path = f"{encryption_folder}encryption.txt"
    if os.path.isdir(encryption_folder) is False:
        os.mkdir(encryption_folder)
    with open(encryption_path) as file:
        data = file.readlines()
        
    if get_length(data) < 1:
        for item in characters:
            encryption[item] = generate_random(5)
        
        with open(f"{encryption_path}", "a") as file:
            file.write("ENCRYPTION STORAGE\n")
            file.write("="*18)
            for key, value in encryption.items():
                file.write(f"\n{key}:{value}")

    def encrypt_password(password: str) -> str:
        '''
        Hash password based on passed argument and return the hash.
        '''
        encryption = {}
        data = None
        with open(HashPass.encryption_path) as file:
            data = file.readlines()
        for lines in data:
            if ":" in lines:
                splitted = split(lines, ":", "\n")
                encryption[splitted[0]] = splitted[1]
            
        hashed_password = ""
        for character in password:
            if character in encryption:
                hashed_password += encryption[character]
        
        return hashed_password
    
    def decrypt_password(plain_password: str, hashed_password: str) -> bool:
        '''
        Description - Compare plain password with the hash. Returns a boolean
        '''
        plain_password = HashPass.encrypt_password(plain_password)
        
        if plain_password == hashed_password:
            return True
        else:
            return False 

def auth_system() -> None:
    from advanced_expense_tracker import remove_trailing_space
    
    user_storage_folder = "./data_files/"
    user_storage_file = "user.txt"
    full_file_path = user_storage_folder + user_storage_file
    
    if os.path.isdir(user_storage_folder) is True:
        pass
    else:
        os.mkdir(user_storage_folder)
    # if os.path.exists(full_file_path) is False:
    #     os.path.join(user_storage_folder, user_storage_file)
    
    def dashBoard(username: str) -> None:
        print(f"\nWelcome,{username}")
        while True:
            prompt = remove_trailing_space(input("\nLogout yes/no: "))
            if prompt.lower() == "yes":
                print("\nLog out successful")
                break
        
  
    while True:
        print("\nMenu")
        print("="*4)
        
        menu_list = ["Register", "Login", "Exit"]
        
        for i in range(get_length(menu_list)):
            print(f"Enter {i + 1} to {menu_list[i]}")
            
        option_selected = remove_trailing_space(input("Enter your selected option: "))
        
        if option_selected == "1":
            while True:
                data = None
                username = remove_trailing_space(input("\nEnter username: "))
                if get_length(username) < 4 :
                    print("\nUsername length must be greater than 4..")
                    continue
                with open(full_file_path) as file:
                    data = file.readlines()
                    
                for line in data:
                    existing_user = split(line, ",", ":")
                    if get_length(existing_user) > 0:
                        if username == existing_user[0]:
                            print("\nuser with username already exist, enter another username..\n")
                            break
                else:
                    break
            password = remove_trailing_space(input("\nEnter password: "))
            hashed_password = HashPass.encrypt_password(password)
            
            with open(full_file_path, "a") as file:
                file.write(f"{username}:{hashed_password}\n")
                
            print("\nUser registration successful..")
        
        if option_selected == "2":
            print("\nLOGIN PAGE")
            print("="*9)
            
            tries = 3
            while tries != 0:
                data = None
                username = remove_trailing_space(input("\nEnter username: "))
                with open(full_file_path) as file:
                    data = file.readlines()
                user = None  
                for lines in data:
                    user = split(lines, ":", "\n")
                    if username == user[0]:
                    
                        password = remove_trailing_space(input("\nEnter password: "))
                        compare_password = HashPass.decrypt_password(password, user[1])
                        if compare_password:
                            print("\nUser login successful")
                            dashBoard(user[0])
                            tries = 0
                            break
                else:
                    tries -= 1
                    print(f"\nInvalid credentials, you have {tries} tries left. ")
               
                    
        if option_selected == "3":
            print("\nYou've exited the program....")
            break
        
auth_system()
                
    