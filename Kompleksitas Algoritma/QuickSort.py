def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:
        if x[1] <= pivot[1]:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [('Andi', 78), ('Budi', 65), ('Tono', 85), ('Dewi', 72), ('Eka', 90)]

sorted_arr = quick_sort(arr)

for name, value in sorted_arr:
    print(name, value)