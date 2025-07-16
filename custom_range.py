from most_frequent import get_length
def custom_range(start: int = 0, end: int = 0, step: int = None) -> list:
    my_list: list = []
    
    if start and not end:
        end = start
        start = 0
        
    if start < end:
        my_list.append(start)
        while start < end:
            if step:
                start += step
            else:
                start += 1
            if start < end:
                my_list.append(start)
        else:
            return my_list
                
    if start > end:
        my_list.append(start)
        while start > end:
            if step:
                start += step
            else:
                start -= 1
            if start > end:
                my_list.append(start)
                
    if get_length(my_list) == 0:
        return None
    return my_list

    
print(custom_range(1, 10))
# numbers = [10, 20, 30, 40, 50]
# for i in custom_range(2,get_length(numbers)):
#     print(numbers[i])

