def max_abs_val(lst):
    largest_number=abs(lst[0])
    for num in lst[1:]:
        if (largest_number<abs(num)):
            largest_number=abs(num)
    return largest_number