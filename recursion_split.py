def split(string : str, split_by : str) -> list:
    new_list = []
    current_index = 0
    for i in range(len(string)):
        if string[i] in split_by:
                new_list.append(string[current_index:i])
                current_index = i + 1
    if current_index < len(string):
        new_list.append(string[current_index:])
    return new_list
 
print(split("HELLO HOW. ARE YOU Have you seen your people.", " "))
            
            