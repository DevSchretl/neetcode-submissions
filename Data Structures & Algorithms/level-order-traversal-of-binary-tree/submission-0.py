# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if (root == None):
            return [];
        
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        combined = [[root.val]]

        if len(left) < len(right):
            for i in range(len(left)):
                combined.append(left[i] + right[i])
            combined = combined + right[len(left):]
        else:
            for i in range(len(right)):
                combined.append(left[i] + right[i])
            combined = combined + left[len(right):]
        
        return combined

        