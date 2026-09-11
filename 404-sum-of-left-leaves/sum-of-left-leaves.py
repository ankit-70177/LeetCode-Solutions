# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=0
        def fun(root):
            nonlocal ans
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                ans+=root.left.val
            fun(root.left)
            fun(root.right)

        fun(root)
        return ans
        