# ✅ Challenge: Manual Bubble Sort
# Write a function called bubble_sort that:

# 1️⃣ Takes a list of integers as input.
# 2️⃣ Sorts the list in ascending order using the bubble sort algorithm.
# 3️⃣ Does not use sorted(), sort(), or any built-in sorting helpers.
# 4️⃣ Returns the sorted list.

def bubble_sort(interger_list : list[int]) -> list:
    from most_frequent import get_length
    
    # MY VERSION
    
    # for i in range(get_length(interger_list)):
    #     for j in range(get_length(interger_list) - i - 1):
    #         left_side_value = interger_list[i]
    #         right_side_value = interger_list[j]
    #         if right_side_value < left_side_value:
    #             temporary_left_value = left_side_value
    #             interger_list[i] = right_side_value
    #             interger_list[j] = temporary_left_value
    # return interger_list
        
    length = get_length(interger_list)
    for i in range(length): #(0, 4)
        for j in range(0,length - i - 1): #(0, 4), 2
            left = interger_list[j] #0
            right = interger_list[j + 1] #1           #[5, 10, 20, 30, 70]
            if left > right:
                interger_list[j], interger_list[j + 1] = right, left
    
    return interger_list 

if __name__ == "__main__":
    numbers = [20, 5, 2, 9, 1, 5, 6]

    print(bubble_sort(numbers))



