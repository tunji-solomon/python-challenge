# ✅ Challenge: Safe Divider Function
# Write a function called safe_divide that:

# 1️⃣ Takes two arguments, a and b (both should be numbers).
# 2️⃣ Tries to divide a by b.
# 3️⃣ If b is zero, handle the ZeroDivisionError by printing:
# "Cannot divide by zero." and return None.
# 4️⃣ If a or b is not a number, handle the TypeError by printing:
# "Both inputs must be numbers." and return None.
# 5️⃣ If everything is fine, return the result.

def safe_divide(a, b) -> int:
    
    #this is one way to do it 
    # try:
    #     result = a / b
    #     return result
    # except ZeroDivisionError:
    #     return "Cannot divide by zero"
    # except TypeError:
    #     return "Both values must be a number"
    
    #i want to handle everything manually doing this
    if b == 0:
        return "Output: Cannot divide by zero."
    
    elif type(a) == (int or float) and type(b) == (int or float):
        result = a / b
        return f"Output: {result}"
    else:
        return "Output: Both inputs must be a number."

print(safe_divide(10, 2.5)) # Output: 5.0
print(safe_divide(10, 0)) # Output: Cannot divide by zero.
print(safe_divide(10, "a")) # Output: Both inputs must be numbers.

