# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        temp = []
        answer = []

        while root or temp:
            while root:
                temp.append(root)
                root = root.left
            
            root = temp.pop()
            answer.append(root.val)

            root = root.right
        
        return answer 