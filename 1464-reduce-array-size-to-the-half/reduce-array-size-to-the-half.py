class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        val=len(arr)
        target=len(arr)//2
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        new=[]
        for i in freq.values():
            new.append(i)
        new.sort(reverse=True)
        ans=0
        for i in new:
            if val>target:
                val-=i
                ans+=1
            else:
                break
        return ans
        