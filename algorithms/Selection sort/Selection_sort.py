def selection_sort(lst):
    size = range(0,len(lst)-1)

    for i in size:
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[min] , lst[i] = lst[i], lst[min]

    return lst


print(selection_sort([2,3,5,1,5,3,9,7,56,4,8]))