''' Postorder traversal is another depth-first traversal method.
In postorder, the nodes are visited in this order:

1. Traverse the **Left Subtree**
2. Traverse the **Right Subtree**
3. Visit the **Root**

'''

class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class Solution:
   
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.data)
        

    def postorderTraversal(self,root):
        self.ans=[]
        self.postorder(root)
        return self.ans
    





# -------- Create Tree --------
# Example Tree:
#         1
#        / \
#       2   3
#      / \
#     4   5


# root = TreeNode(1)
# root.left=TreeNode(2)
# # root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.left.right=TreeNode(5)
# root.left.left=TreeNode(4)
# root.right = TreeNode(3)

root= TreeNode(1,
               TreeNode(2,TreeNode(4),TreeNode(5,None,TreeNode(6))),
               TreeNode(3,None,TreeNode(7,None,TreeNode(8))))

# -------- Run Preorder Traversal --------
sol = Solution()
result = sol.postorderTraversal(root)
print("Postorder Traversal:", result)  # Output: [4,5,2,3,1]
