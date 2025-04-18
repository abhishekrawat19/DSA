# WAJP to  swap two index values of the array.

def swaptwo(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

    return arr


print("New array",swaptwo([1,2,4,3],2,3))



