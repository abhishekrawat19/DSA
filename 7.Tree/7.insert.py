class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def insert(self,root,target):
        curr=root
        newnode=TreeNode(target)
        if root is None:
            return newnode

        while curr!=None:
            if target < curr.val:
                if curr.left != None:
                    curr=curr.left

                else:
                    curr.left=newnode
                    break

            else:
                if curr.right!=None:
                    curr=curr.right
                else:
                    curr.right=newnode
                    break


# BST Structure (Manual Creation)
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

sol = Solution()
print("insert element is ,",sol.insert(root,40))


'''
        50
       /  \
     30    70
    / \    / \
  20 40  60 80

'''