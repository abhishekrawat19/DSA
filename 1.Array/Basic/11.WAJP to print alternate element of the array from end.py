# WAJP to print alternate element of the array from end.

def alternate(arr):
    
    for i in range(0,len(arr),2):
        print(arr[i])

alternate([12,2,12,1,12,4,12,1])