class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x=max(nums)
        ans=0
        for i in range(len(nums)):
            ans+=x-nums[i]
        return ans
        