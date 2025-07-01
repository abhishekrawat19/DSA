class Stack:
    def __init__(self):
        self.st=[]


    def push(self,x):
        self.st.append(x)

    def pop(self):
        if len(self.st)==0:
            return -1
        
        x=self.st[-1]
        self.st.pop()
        return x
    
    def top(self):
        if len(self.st)==0:
            return -1
        print(self.st[-1])
    
    def size(self):
        return len(self.st)
    



stack=Stack()
stack.push(1)
stack.top()
stack.push(2)
stack.top()
stack.push(3)
stack.top()
print(f"Size of Stack {stack.size()}")
print(stack.pop())
print(f"Size of Stack {stack.size()}")
print(stack.pop())
print(f"Size of Stack {stack.size()}")