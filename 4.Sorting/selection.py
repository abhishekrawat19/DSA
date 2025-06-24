# SELECTION SORT


def sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

    return arr


print(sort([12,7,8,9,4]))