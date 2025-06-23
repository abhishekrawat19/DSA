# WAJP to rotate each element of an array by one position in right side.

def RotateOne(arr):
    n=len(arr)
    last=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
    print(arr)


RotateOne([1,2,3,4,5])
