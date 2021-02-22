def avg_val(lst):
    avg=sum(lst)/len(lst)
    if (avg%1==0):
        avg=int(avg)
    return avg