# WAJP to reverse each element of the array.

def reverse(arr):
    lastIndex=len(arr)-1
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i]=arr[lastIndex-i]
        arr[lastIndex-i]=temp

    return arr


print(reverse([1,2,3,4,5]))
print(reverse([12,3,4,5,63,53]))