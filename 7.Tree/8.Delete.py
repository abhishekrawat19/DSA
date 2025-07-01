class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def delete(self,root,key):
        curr=root
        if root is None:
            return None
        
        if key<root.val:
            root.left=self.delete(root.left,key)
        elif key>root.val:
            root.right=self.delete(root.right,key)
        else: # key ==root.val
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp=root.right
                while temp.left!=None:
                    temp=temp.left
                
                root.val=temp.val
                root.right=self.delete(root.right,temp.val)


       
# BST Structure (Manual Creation)
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

sol = Solution()
print("delete element is ,",sol.delete(root,40))

