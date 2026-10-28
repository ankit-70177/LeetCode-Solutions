class Solution:
    def frequencySort(self, s: str) -> str:
        freq_count={}
        for i in s:
            if i in freq_count:
                freq_count[i]+=1
            else:
                freq_count[i]=1
        ans=[]
        i=0
        for key in freq_count:
            ans.append([freq_count[key],key])
            i+=1
        ans.sort(reverse=True)
        final_s=""
        for i in ans:
            final_s+=i[0]*i[1]
        return final_s
        
        