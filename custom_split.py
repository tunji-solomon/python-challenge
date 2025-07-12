def split(string : str, *split_by : tuple) -> list:
    new_list = []
    current_index = 0
    for i in range(len(string)):
        if string[i] in split_by:
                new_list.append(string[current_index:i])
                current_index = i + 1
    if current_index < len(string):
        new_list.append(string[current_index:])
    return new_list
 
if __name__ == "__main__":
    split()            
            