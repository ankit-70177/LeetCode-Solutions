# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        def average(root):
            if not root:
                return 0,0
            left_sum,left_count=average(root.left)
            right_sum,right_count=average(root.right)
            total_sum=left_sum + root.val + right_sum
            total_count=left_count + 1 + right_count

            return total_sum,total_count
        
        def fun(root):
            nonlocal ans
            if not root:
                return
            su,count=average(root)
            avg=su//count
            if root.val==avg:
                ans+=1
            fun(root.left)
            fun(root.right)
        fun(root)
        return ans

        