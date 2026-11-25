import sys
sys.setrecursionlimit(10**6)
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        dp=[]
        for i in range(n):
            dp.append([-float('inf')]*n)
        def fun(i,j):
            if j<0 or j>=n:
                return float('inf') 
            if i==n-1:
                return matrix[i][j]
            if dp[i][j]==-float('inf'):
                down=fun(i+1,j)
                down_left=fun(i+1,j-1)
                down_right=fun(i+1,j+1)
                dp[i][j]=min(down,down_left,down_right)+matrix[i][j]
            return dp[i][j]
        ans=float('inf')
        for i in range(n):
            ans=min(ans,fun(0,i))
        return ans
