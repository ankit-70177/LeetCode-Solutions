class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # def find(val):
        #     for i in knowledge:
        #         if i[0]==val:
        #             return i[1]
        #     return "?"
        dic = {}
        for i in knowledge:
            dic[i[0]]=i[1]
        ans=""
        i=0
        while i<len(s):
            if s[i]!="(":
                ans+=s[i]
            elif s[i]=="(":
                val=""
                for j in range(i+1,len(s)):
                    if s[j]==")":
                        i=j
                        break
                    val+=s[j]
                if val in dic.keys():
                    ans+=dic[val]
                else:
                    ans+="?"
            i+=1
        return ans

                