class Solution:
    def reverseDegree(self, s: str) -> int:
        dic={}
        for i in range(1,27):
            dic[chr(123-i)]=i
        ans=0
        for i in range(len(s)):
            ans+=dic[s[i]]*(i+1)
        return ans