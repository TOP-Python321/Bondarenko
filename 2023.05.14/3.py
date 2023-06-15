def numbers_strip(numbers_list, n = 1, return_copy = False):
    sorted_numbers = sorted(numbers_list)
    stripped_numbers = sorted_numbers[n:len(sorted_numbers)-n]
    if return_copy:
        return stripped_numbers.copy()
    else:
        numbers_list.clear()
        numbers_list.extend(stripped_numbers)
        return numbers_list
        

