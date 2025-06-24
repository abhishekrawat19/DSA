# QUICK SORT

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr


def partition(arr, start, end):
    mid = start + (end - start) // 2
    pivot = arr[mid]

    # Move pivot to end
    swap(arr, mid, end)

    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Place pivot in its correct position
    swap(arr, i + 1, end)
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# Test
arr = [12, 4, 6, 6, 2, 1, 4]
n = len(arr)
print("Sorted array:", quick_sort(arr, 0, n - 1))
