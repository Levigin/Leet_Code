from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, node: Optional[TreeNode], target_sum: int) -> bool:
        if node is None:
            return False
        if node.left is None and node.right is None:
            return target_sum == node.val
        return self.hasPathSum(node.left, target_sum - node.val) or self.hasPathSum(node.right, target_sum - node.val)
