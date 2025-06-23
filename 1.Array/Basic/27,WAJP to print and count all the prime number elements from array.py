# WAJP to print and count all the prime number elements from array.

def primecount(arr):
    count=0
    li=[]
    for i in range(0,len(arr)):
        digit=1
        if arr[i]==2:
            count+=1

        for j in range(2,arr[i]):
            if arr[i]%j==0:
                digit+=1
                break

        if digit == 2:
            count=count+1
        else:
           li.append(arr[i])

    return count,li
    

print(primecount([2,3,4,5,6]))


