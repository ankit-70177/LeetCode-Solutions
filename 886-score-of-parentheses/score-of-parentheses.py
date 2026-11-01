class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        curr=0
        for i in s:
            if i=="(":
                stack.append(curr)
                curr=0
            else:
                if curr==0:
                    curr+=1
                else:
                    curr*=2
                curr+=stack.pop()
        return curr


        