# WAJP to rotate all the elements of array k position to its right.


def RotateOne(arr,k):
    n=len(arr)

    for j in range(0,k):
        last=arr[n-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=last
    print(arr)


RotateOne([1,2,3,4,5],2)
