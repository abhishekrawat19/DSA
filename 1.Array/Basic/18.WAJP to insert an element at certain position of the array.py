# WAJP to insert an element at certain position of the array.

def insert_element(arr,pos,ele):
    b=[0]*(len(arr)+1)
    if pos == len(arr):
        arr.append(ele)
        return arr
    for i in range(len(arr)):
        if i < pos:
            b[i] = arr[i]  # Copy elements before the insertion point
        else:
            b[i + 1] = arr[i]  # Shift elements after the insertion point
    
    b[pos] = ele  # Insert the new element at the specified position
    
    return b
   
x=insert_element([1,2,3,4,5,6,7],2,400)
print(x)


