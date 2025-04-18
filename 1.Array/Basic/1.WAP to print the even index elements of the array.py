# WAP to print the even index elements of the array.

def evenIndex(arr):
    for i in range(0,len(arr)):
        if i%2!=0:
            print(arr[i])
    

evenIndex([12,3,11,4,11,5])