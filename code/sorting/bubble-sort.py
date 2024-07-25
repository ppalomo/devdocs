def bubble_sort(arr):

    # loop to access each array element
    for i in range(len(arr)):

        # loop to compare array elements
        for j in range(0, len(arr) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if arr[j] > arr[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


arr = [8, 20, 4, 78, 32, 10, 3, 86, 23, 56, 11, 2]
print(bubble_sort(arr))
