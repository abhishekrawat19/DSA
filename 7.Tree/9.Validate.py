# Validate BST 
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkvalidate(self,root,min,max):
        curr=root
        if root is None:
            return True
        if root.val <min or root.val > max:
            return False
        
        checkleft=self.checkvalidate(root.left,min,root.val-1)
        checkright=self.checkvalidate(root.right,root.val+1,max)

        return checkleft and checkright
    
    def validate(self,root):
        return self.checkvalidate(root,-1000000,100000000000)

            

        



# BST Structure
#       10
#      /  \
#     5   15
#        /  \
#       12  20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

sol=Solution()
v=sol.validate(root)
print(v)