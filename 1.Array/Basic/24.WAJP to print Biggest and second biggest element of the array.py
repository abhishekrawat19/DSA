def biggestnum(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"

    max1 = float('-inf')
    max2 = float('-inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:  # no check for distinctness here
            max2 = num

    if max2 == float('-inf'):
        max2 = max1

    return max1, max2

print(biggestnum([12, 12, 6]))  # Output: (12, 12)
