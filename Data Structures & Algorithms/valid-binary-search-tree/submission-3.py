# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], upper=None, lower=None) -> bool:
        if root is None:
            return True

        if upper is not None:
            if root.val >= upper:
                return False
        if lower is not None:
            if root.val <= lower:
                return False
        
        return self.isValidBST(root.left, root.val, lower) and self.isValidBST(root.right, upper, root.val)
        
      
        
        