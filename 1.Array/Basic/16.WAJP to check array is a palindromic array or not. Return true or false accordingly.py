
# WAJP to check array is a palindromic array or not. Return true or false accordingly.
def palindrome(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            return False

    return True

# Test
a = [1, 2, 3,4,5,4, 2, 1]
x = palindrome(a)

if x:
    print("is palindrome")
else:
    print("false")

