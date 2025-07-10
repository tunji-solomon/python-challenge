
# ✅ Challenge: Flatten a Nested List
# Write a function called flatten_list that:

# 1️⃣ Takes a list that can contain integers or other lists (nested arbitrarily deep).
# 2️⃣ Returns a new flat list with all the integers in order.
# 3️⃣ Uses recursion — no sum() tricks, no itertools.chain.

# 💡 Rules TO FOLLOW
# Use recursion to handle the fact that lists can be nested arbitrarily deep.

# Do not use any built-in flatten helpers.

# Use loops, type checks, and your own logic only.


def flatten_list(nested_list: list[int, list]) -> list:
    
    from bubble_sort import bubble_sort
    from most_frequent import get_length
    
    
    for i in range(get_length(nested_list)):
        if type(nested_list[i]) == list:
            for item in nested_list[i]:
                nested_list.append(item)
            nested_list[i:i+1] = []
            return flatten_list(nested_list)
    else:
        nested_list = bubble_sort(nested_list)
        return nested_list
                

nested1 = nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
nested2 = [1, [17, 20, [18]], [2, 16, 3, [4, [10], 5, [15, 19]]], 6, [7, [8, 9, [11, [12, 13, [14]]]]]]

print(flatten_list(nested1))
print(flatten_list(nested2))
        
            