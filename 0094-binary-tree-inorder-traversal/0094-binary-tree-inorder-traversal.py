#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []

        def helper(node):
            if node is None:
                return
            
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(root)
        return result