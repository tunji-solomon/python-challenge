
# ✅ Challenge: Recursive Sum of a List
# Write a function called recursive_sum that:

# 1️⃣ Takes a list of integers as input.
# 2️⃣ Uses recursion (no loops!) to calculate and return the sum of all the numbers in the list.
# 3️⃣ You cannot use sum() or loops — only recursion.

def recursive_sum(interger_list: list[int]) -> int:
    
    def get_length(iterable) -> int:
        
        length = 0
        for _ in iterable:
            length += 1
        return length
    
    sum_of_integers = 0
    if get_length(interger_list) == 1:
        sum_of_integers += interger_list[0]
        return sum_of_integers
    
    else:
        sum_of_integers += interger_list[0]
        interger_list[0:1] = []
        return sum_of_integers + recursive_sum(interger_list)

numbers = [1, 2, 3, 4, 5]

print(recursive_sum(numbers))
        
    