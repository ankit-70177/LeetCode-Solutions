class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        s=[]
        def fun(open,close):
            if open==n and close==n:
                ans.append("".join(s))
                return
            if open<n:
                s.append("(")
                fun(open+1,close)
                s.pop()
            if close<open:
                s.append(")")
                fun(open,close+1)
                s.pop()
        fun(0,0)
        return ans


        