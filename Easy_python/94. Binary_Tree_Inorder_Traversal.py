class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def inorder_traversal(root: TreeNode) -> list[int]:
        ans = []

        def rec(r: TreeNode, ans_: list):
            if r is None:
                return None

            rec(r.left, ans_)
            ans_.append(r.val)
            rec(r.right, ans_)

        rec(root, ans)
        return ans
