# WAJP to print the Biggest element, Smallest element and their difference in the array.

def bigSmall(arr):
    big=arr[0]
    small=arr[0]
    for i in range(len(arr)):
        if big<arr[i]:
            big=arr[i]
        if small>arr[i]:
            small=arr[i]

    return big,small


print(bigSmall([12,12,2,4,4,2,1,0]))