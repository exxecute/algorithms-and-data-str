# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        if root is None:
            return answer
        
        q = deque([root])
        
        answer.append([root.val])
        
        while q:
            level = []
            levelSize = len(q)
            
            for _ in range(levelSize):
                currentNode = q.popleft()
                
                if currentNode.left:
                    level.append(currentNode.left.val)
                    q.append(currentNode.left)
                
                if currentNode.right:
                    level.append(currentNode.right.val)
                    q.append(currentNode.right)
            
            if level:
                answer.append(level)
        
        return answer