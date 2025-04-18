# WAJP to print and count all the elements of array which are bigger than  average value.


def averageCount(arr):
    count=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    avg=sum//(len(arr)-1)
    for i in range(len(arr)):
        if avg < arr[i]:
            print(arr[i])
            count+=1

    return count

print(averageCount([12,12,12,12,12,13,16,17,18]))