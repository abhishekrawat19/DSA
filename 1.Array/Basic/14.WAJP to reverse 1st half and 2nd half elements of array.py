# WAJP to reverse 1st half and 2nd half elements of array.

def reversehalf(arr):

    reverse(arr,0,len(arr)//2-1)
    reverse(arr,len(arr)//2,len(arr)-1)

    return arr


def reverse(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1


print(reversehalf([12,12,2,3,5,4,3,5]))