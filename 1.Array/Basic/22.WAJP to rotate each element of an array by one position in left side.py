# WAJP to rotate each element of an array by one position in left side.

def leftRotate(arr):
    n=len(arr)
    first=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=first

    return arr


print(leftRotate([1,2,3,4,5]))