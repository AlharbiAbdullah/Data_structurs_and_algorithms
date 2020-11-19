def merg(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left, right = merg(arr[:mid]) , merg(arr[mid:])
    return sorting(left,right)


def sorting(left, right):
    sorted = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted


# testing

arr = [2, 76, 6, 45, 8, 5, 3, 0]

print(merg(arr))