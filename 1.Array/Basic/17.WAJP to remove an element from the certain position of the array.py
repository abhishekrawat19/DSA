
#WAJP to remove an element from the certain position of the array.

def remove_element(arr,pos):
    b=[]
    if len(arr)<pos:
        return False
    for i in range(0,len(arr)):
        if i!=pos:
            b.append(arr[i])    
    return b


x=remove_element([12,23,34,32,44],0)
print(x)
        