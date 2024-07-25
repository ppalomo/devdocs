def binary_search(x, arr, low=None, high=None):

    low = 0 if not low else low
    high = len(arr) - 1 if not high else high

    if low <= high:
        mid = low + (high - low) // 2

        # If found at mid, then return it
        if arr[mid] == x:
            return mid

        # Search the right half
        elif arr[mid] < x:
            return binary_search(x, arr, mid + 1, high)

        # Search the left half
        else:
            return binary_search(x, arr, low, mid - 1)

    return -1


arr = [2, 3, 4, 8, 10, 11, 20, 23, 32, 56, 78, 86]
print(binary_search(56, arr))
