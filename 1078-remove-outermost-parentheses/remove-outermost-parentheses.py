class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=0
        ans=[]
        temp=""
        for i in s:
            if i=="(":
                temp+=i
                stack+=1
            elif i==")":
                temp+=i
                stack-=1
            if stack==0:
                ans.append(temp[1:len(temp)-1])
                temp=""
        return "".join(ans)

