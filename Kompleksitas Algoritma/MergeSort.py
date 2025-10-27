def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)

def merge(left, right):
    nL, nR = len(left), len(right)
    i = j = 0
    result = []

    while i < nL and j < nR:
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < nL:
        result.extend(left[i:])
    if j < nR:
        result.extend(right[j:])
    return result

arr = [('Andi', 78), ('Budi', 65), ('Tono', 85), ('Dewi', 72), ('Eka', 90)]

sorted_arr = mergeSort(arr)

for name, value in sorted_arr:
    print(name, value)