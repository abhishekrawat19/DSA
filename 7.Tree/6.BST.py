class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class Solution:

    def bstSearch(self,root,target):
        curr=root
        while curr!=None:
            if curr.val == target:
                return curr.val
            elif curr.val > target:
                curr=curr.left
            else:
                curr=curr.right

        return None







# BST Structure (Manual Creation)
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

sol = Solution()
print("Search element is ,",sol.bstSearch(root,40))


'''
        50
       /  \
     30    70
    / \    / \
  20 40  60 80

'''