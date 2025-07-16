import os
from most_frequent import get_length
from custom_split import split
import json

with open("./data_files/expense.json") as file:
    data = file.readlines()
    
my_list = []
for line in data:
    line = line.strip()
    if line[0] in ["{", "}"]:
        continue
    splitted = split(line, "{", "}")
    if len(splitted[0]) > 2:
        for character in splitted[0]:
            if character == "[" or character == "]":
                splitted[0] = splitted[0].strip(character).strip()
        my_list.append(splitted)
    

print(my_list)
# my_list = []   
# for data in data:
#     if get_length(data) == 0:
#         continue
#     if data[0] in ["{", "}"]:
#         continue
#     splitted = split(data, "\n", "")
#     my_list.append(splitted)

# print(my_list)  
# modified = []
# for i in my_list:
#     if " " in i or "" in i:
#         continue
#     else:
#         modified.append(i)
    
    
# print(modified)