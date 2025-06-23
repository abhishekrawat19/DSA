# For the given array of Strings, print and count all the Strings which has even number of characters.

def strcount(arr):
    count=0
    for i in range(len(arr)):
        if len(arr[i])%2==0:
            print(arr[i])
            count+=1

    return count


print(strcount(['abhi','shek','han']))
        