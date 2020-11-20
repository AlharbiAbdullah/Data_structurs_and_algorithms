def insertion_sort(lst):
    size = range(1,len(lst))
    for i in size:
        value = lst[i]

        while lst[i-1] > value and i > 0:
            lst[i] , lst[i-1] = lst[i-1] , lst[i]
            i = i - 1
    return lst

# test
print(insertion_sort([3,5,7,3,1,2,10,44,6,8]))