# WAJP to check no is even or odd without using if else/Conditional Operator statement 

def evenodd(arr):
    s = 'even','odd'
    for i in range(0,len(arr)):
        if arr[i]%2==0:
            print(s[0]+str(arr[i]))
        else:
            print(s[1]+str(arr[i]))

def evenod(arr):
    result = ['even', 'odd']
    for num in arr:
        print(f"{result[num % 2]} {num}")


evenodd([12, 13, 12, 15])
evenod([12,13,12,15])