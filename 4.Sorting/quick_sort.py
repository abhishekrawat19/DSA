# QUICK SORT

def quick_sort(arr,start,end):
    if(end>start):
        pivot=partition(arr,start,end)
        quick_sort(arr,start,pivot-1)
        quick_sort(arr,pivot+1,end)

    return arr


def partition(arr,start,end):
    pivot=arr[start]
    i=start
    j=end

    while(i<=j):

        while(i<=j and arr[i]<=pivot):
            i=i+1

        while(i<=j and arr[j]>=pivot):
            j=j-1

        if(i<j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

    
    arr[start],arr[j]=arr[j],arr[start]    
    return j

arr = [4, 2, 7, 1, 9, 3]
print(quick_sort(arr, 0, len(arr)-1))
