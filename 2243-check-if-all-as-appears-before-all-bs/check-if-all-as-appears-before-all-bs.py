class Solution:
    def checkString(self, s: str) -> bool:
        c_b=0
        for i in s:
            if i=="a":
                if c_b!=0:
                    return False
            else:
                c_b+=1
        return True



        