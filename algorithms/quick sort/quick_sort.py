def quickSort(lst):
    size = len(lst)
    if size <= 1:
        return lst  # return any list that empty or has 1 or less values.

    else:
        pivot = lst.pop()  # taking the last element as pivot

    lower_lst = []
    greater_lst = []
    for item in lst:
        if item > pivot:
            greater_lst.append(item)
        else:
            lower_lst.append(item)

    # return a recursive call until the list is sorted
    return quickSort(lower_lst) + [pivot] + quickSort(greater_lst)

print(quickSort([4,5,76,6,45,33,5,2,2]))