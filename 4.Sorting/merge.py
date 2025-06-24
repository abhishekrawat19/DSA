def merge_sort(arr, start, end):
    # Base case: if the subarray has less than 2 elements, it's already sorted
    if end > start:
        mid = start + (end - start)// 2

        # Recursively sort left and right halves
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)

        # Merge the sorted halves
        merge(arr, start, mid, end)

    return arr


def merge(arr, start, mid, end):
    merged = []  # Temporary list for merged elements
    left_index = start      # Pointer for left half
    right_index = mid + 1   # Pointer for right half

    # Merge the two sorted halves
    while left_index <= mid and right_index <= end:
        if arr[left_index] < arr[right_index]:
            merged.append(arr[left_index])
            left_index += 1
        else:
            merged.append(arr[right_index])
            right_index += 1

    # Copy any remaining elements from left half
    while left_index <= mid:
        merged.append(arr[left_index])
        left_index += 1

    # Copy any remaining elements from right half
    while right_index <= end:
        merged.append(arr[right_index])
        right_index += 1

    # Copy merged elements back into original array
    for i in range(len(merged)):
        arr[start + i] = merged[i]



arr = [1, 8, 7, 6, 9, 4]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
