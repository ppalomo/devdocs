def binary_search(x, arr):

    low = 0
    high = len(arr) - 1

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        # If found at mid, then return it
        if arr[mid] == x:
            return mid

        # Search the right half
        elif arr[mid] < x:
            low = mid + 1

        # Search the left half
        else:
            high = mid - 1

    return -1


arr = [2, 3, 4, 8, 10, 11, 20, 23, 32, 56, 78, 86]
print(binary_search(11, arr))
