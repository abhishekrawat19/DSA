# 


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=Node(5)
root.left=Node(1)
root.right=Node(12)
root.right.left=Node(8)

print(root.right.data)
print(root.right.left.data)