
# ✅ Challenge: Remove Duplicates from a List
# Write a function called remove_duplicates that:

# 1️⃣ Takes a list of items (can be strings, numbers, or mixed).
# 2️⃣ Returns a new list with the duplicates removed — keeping only the first occurrence of each item.
# 3️⃣ The order of the items should stay the same as the original.

def remove_duplicates(item_list : list) -> list:
    
    def counter(word: str) -> int: #I defined this function to subtitute for the built in len function.
        count = 0
        for _ in word:
            count += 1
        return count
    
    def isExist (variable, iterable) -> bool:
        i = 0
        while i < counter(iterable):
            if variable == iterable[i]:
                return True
            i += 1

        else:
            return False
    
    
    unique_item = []
        
    for item in item_list:
        if isExist(item, unique_item) == False:
            unique_item.append(item)
        
    return unique_item

items = [1, 2, 2, 3, 4, 3, 5, "hello", "Hello", "hello"]

print(remove_duplicates(items))