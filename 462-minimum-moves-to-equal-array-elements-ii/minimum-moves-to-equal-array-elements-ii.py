class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        i=mid-1
        j=mid+1
        ans=0
        while i>=0:
            ans+=nums[mid]-nums[i]
            i-=1
        while j<=len(nums)-1:
            ans+=nums[j]-nums[mid]
            j+=1
        return ans
