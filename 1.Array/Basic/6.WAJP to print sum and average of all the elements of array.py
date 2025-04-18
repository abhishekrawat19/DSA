# WAJP to print sum and average of all the elements of array.

def sumAverage(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    avg=sum//(len(arr)-1)
    return sum,avg

print(sumAverage([12,12,12,12,12]))