''' 
Preorder traversal is one of the Depth-First Traversal methods for binary trees.
In preorder, the nodes are visited in this exact order:

1. Visit the **Root**
2. Traverse the **Left Subtree**
3. Traverse the **Right Subtree**

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # ans = []

    def preorder(self, root):
        if root is None:
            return
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans


# -------- Create Tree --------
# Example Tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left=TreeNode(2)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.left.right=TreeNode(5)
root.left.left=TreeNode(4)
root.right = TreeNode(3)

# -------- Run Preorder Traversal --------
sol = Solution()
result = sol.preorderTraversal(root)
print("Preorder Traversal:", result)  # Output: [1, 2, 4, 5, 3]
