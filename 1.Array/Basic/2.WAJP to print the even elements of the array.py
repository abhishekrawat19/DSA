# WAJP to print the even elements of the array.

def evenElements(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            print(arr[i])


evenElements([12,3,4,2,2])