class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[]
        for i in range(n):
            temp=[]
            for j in range(2):
                temp.append([-1]*3)
            dp.append(temp)

        def fun(i,holding,time):
            if i==len(prices) or time==0:
                return 0
            if dp[i][holding][time]!=-1:
                return dp[i][holding][time]
            if holding == 0:
                
                buy=-prices[i]+fun(i+1,1,time)
                skip=fun(i+1,0,time)
                dp[i][holding][time]=max(buy,skip)
            elif holding == 1:
                
                sell=prices[i]+fun(i+1,0,time-1)
                skip=fun(i+1,1,time)
                dp[i][holding][time]=max(sell,skip)
            return dp[i][holding][time]
        return fun(0,0,2)
            
            

            
        