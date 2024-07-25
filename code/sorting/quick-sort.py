def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    smaller, equal, larger = [], [], []

    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    return quick_sort(smaller) + equal + quick_sort(larger)


arr = [8, 20, 4, 78, 32, 10, 3, 86, 23, 56, 11, 2]
print(quick_sort(arr))
