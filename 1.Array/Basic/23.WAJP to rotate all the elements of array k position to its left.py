# WAJP to rotate all the elements of array k position to its left.

def leftRotate(arr,k):
    n=len(arr)
    for i in range(0,k):
        first=arr[0]
        for i in range(1,n):
            arr[i-1]=arr[i]
        arr[n-1]=first

    return arr


print(leftRotate([1,2,3,4,5],2))