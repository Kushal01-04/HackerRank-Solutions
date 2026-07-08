def average(array):
    # your code goes here
    set_num = set(array)
    avg = sum(set_num)/len(set_num)
    return round(avg,3)

