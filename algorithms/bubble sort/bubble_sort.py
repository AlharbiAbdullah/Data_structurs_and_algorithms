def bubble(arr):
    size = len(arr) - 1   # -1 becuase we dont need to use the last element
    sorted = False  # a logic to check if the list is sorted

    while not sorted:
        sorted = True
        for i in range(0,size):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
    return arr

# test case:

lst = [3,5,7,4,2,6,9,1]

print(bubble(lst))