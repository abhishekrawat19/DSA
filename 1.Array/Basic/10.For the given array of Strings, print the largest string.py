# For the given array of Strings, print the largest string.

def largestStr(arr):
    largelength=len(arr[0])
    for i in range(len(arr)):
        if largelength < len(arr[i]):
            index=i

    return arr[index]


print(largestStr(['abhishek','amit','hi','rawat','rahulgaurav']))