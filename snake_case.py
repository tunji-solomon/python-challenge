# ✅ Challenge: Camel Case to Snake Case Converter
# Write a function called camel_to_snake that:

# 1️⃣ Takes a single camelCase string as input.
# 2️⃣ Converts it to snake_case, inserting underscores before capital letters (except the first one if it’s lowercase).
# 3️⃣ Makes the entire result lowercase.

from most_frequent import get_length
def camel_to_snake(text: str) -> str:
    
    modified_text = ''
    for i in range(get_length(text)):
        if i == 0:
            modified_text += text[i].lower()
        else: 
            if text[i] == text[i].upper():
                modified_text += "_"
                modified_text += text[i].lower()
            else: 
                modified_text += text[i]
                
    return f"Output: {modified_text}"

print(camel_to_snake("helloWorld"))  
print(camel_to_snake("myVariableName"))
print(camel_to_snake("simpleTest")) 
print(camel_to_snake("TestCase"))

        
