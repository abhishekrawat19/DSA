# WAJP to print and count all the three digit numbers of the array.

def threeDigit(arr):
    count=0
    for i in range(len(arr)):
        
        digit=0
        num=arr[i]
        while(num!=0):
            num=num//10
            digit=digit+1
        if digit == 3:
            print(arr[i])
            count=count+1

    return count


print(threeDigit([123,123,123,12]))
            