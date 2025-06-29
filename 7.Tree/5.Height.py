# Height of Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

# Create the tree:
#         1
#        / \
#       2   3
#      /
#     4
#    /
#   4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(4)

# Use the Solution class
sol = Solution()
print("Max Depth of Tree:", sol.maxDepth(root))
