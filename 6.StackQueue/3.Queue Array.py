# Array implemtation in Queue


class Queue:
    def __init__(self):
        self.queue=[]
        self.front=-1

    def push(self,x):
        if self.front == -1:
            self.front=0
        self.queue.append(x)

        return x

    def pop(self):
        if len(self.queue)==0:
            return -1
        x=self.queue[self.front]
        self.front+=1
        if self.front==len(self.queue):
            self.front = -1
            self.queue=[]
        

        return x

    def top(self):
        if len(self.queue)==0:
            return -1
        
        return self.queue[self.front]
    




q=Queue()
print(f"Element is poped is {q.pop()}")
print(f"Element is push {q.push(1)}")
print(f"Element is push {q.push(2)}")
print(f"Element is push {q.push(3)}")


print(f"Element at front is {q.top()}")
print(f"Element is poped is {q.pop()}")

print(f"Element at front is {q.top()}")
print(f"Element is poped is {q.pop()}")

print(f"its zero Element at front is {q.top()}")
print(f"Element is poped is {q.pop()}")

print(f"Element at front is {q.top()}")
print(f"Element is poped is {q.pop()}")

print(f"Element at front is {q.top()}")