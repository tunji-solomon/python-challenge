# ✅ Challenge: Find Most Frequent Number
# Write a function called most_frequent_number that:

# 1️⃣ Takes a list of integers.
# 2️⃣ Counts how many times each number appears.
# 3️⃣ Returns the number that appears the most and its count as a tuple (number, count).
# 4️⃣ If there’s a tie, return any one of the most frequent numbers.


def iterate_by_range(start = False, end = False):
    if start and not end:
        end = start
        start = 0
    if end <= 0:
        return
    else:
        print(start)
        return iterate_by_range(start - 1)
    
def get_length(iterable) -> int:
    length = 0
    for _ in iterable:
        length += 1
    return length
    
# Note: i made the list to accept any type of item
def most_frequent_item(list_of_item : list) -> tuple | list[tuple]: 
    item_counter = {}
    
    #I can choose to do it this way
    
    # for index, item in enumerate(list_of_item):
    #     if type(item) == str:
    #         list_of_item[index] = item.strip().lower()
    
    #But i try to do it manually as much as possible

        
    # check if item is a string, so as to remove trailing white spaces and also make convert all to lowercase
    for i in range(get_length(list_of_item)):
        if type(list_of_item[i]) == str:
            list_of_item[i] = list_of_item[i].strip().lower()
            
    #count number of times an item occured
    for item in list_of_item:
        if item not in item_counter:
                item_counter[item] = 1
        else:
            item_counter[item] += 1
        
    #check for the highest
    highest_occurence = 0
    most_occured_item = None
    isTie = []
    for key, value in item_counter.items():
        if value > highest_occurence:
            highest_occurence = value
            most_occured_item = key
            isTie = []
        if value == highest_occurence:
            isTie.append((key, highest_occurence))
    if len(isTie) > 1: # I put this so i can return all the item that tied has the highest instead of returning one
        return isTie 
    return most_occured_item, highest_occurence

numbers = [1, 2, 2, 3, 3, 4, 4, 4, "python", " Python", "python"]

if __name__ == "__main__":
    print(most_frequent_item(numbers))
        
    
    
            