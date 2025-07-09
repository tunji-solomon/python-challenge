def iterate_by_range(start = False, end = False):
    if start and not end:
        end = start
        start = 0
    if end == 1:
        print(end)
        start += 1
    else:
        print(end)
        return iterate_by_range(end - 1)
    
iterate_by_range(10)