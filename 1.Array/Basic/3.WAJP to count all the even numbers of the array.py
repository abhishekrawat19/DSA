# WAJP to count all the even numbers of the array.

def evenCount(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            count +=1
    return count


print(evenCount([12,12,12,12]))

