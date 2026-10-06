class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans=0
        open=0
        for i in s:
            if open==0:
                if i=="(":
                    open+=1
                else:
                    ans+=1
            elif i=="(":
                open+=1
            else:
                open-=1
        return ans+open


        