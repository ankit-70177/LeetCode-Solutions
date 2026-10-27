class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        mat=[]
        for i in range(m):
            mat.append(["#"]*n)
        a=0
        while a!=n:
            mat[0][a]="."
            a+=1
        for i in range(m):
            mat[i][-1]="."
        ans=[]
        for i in mat:
            ans.append("".join(i))
        return ans
        