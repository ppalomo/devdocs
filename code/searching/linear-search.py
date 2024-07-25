def linear_search(x, arr):

    # Going through array sequencially
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [8, 20, 4, 78, 32, 10, 3, 86, 23, 56, 11, 2]
print(linear_search(99, arr))
