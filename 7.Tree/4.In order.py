# In Order Traversal


class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class Solution:
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.ans.append(root.data)
        self.inorder(root.right)

    def inorderTraversal(self,root):
        self.ans=[]
        self.inorder(root)
        return self.ans
    



root= TreeNode(1,
               TreeNode(2,TreeNode(4),TreeNode(5,None,TreeNode(6))),
               TreeNode(3,None,TreeNode(7,None,TreeNode(8))))

# -------- Run Inorder Traversal --------
sol = Solution()
result = sol.inorderTraversal(root)
print("Inorder Traversal:", result)  # Output: [4,2,5.6.1,3,7,8]
