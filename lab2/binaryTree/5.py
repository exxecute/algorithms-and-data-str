# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return True
            if node.left is not None and node.left.val >= node.val:
                return False
            if node.right is not None and node.right.val <= node.val:
                return False
            return check(node.left) and check(node.right)
        return check(root)