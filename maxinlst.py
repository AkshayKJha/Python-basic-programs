def max_val(lst):
    largest_number=lst[0]
    for num in lst[1:]:
        if (largest_number<num):
            largest_number=num
    return largest_number