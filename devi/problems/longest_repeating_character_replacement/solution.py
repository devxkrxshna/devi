class Solution(object):
    def characterReplacement(self, s, k):
        count={}
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            while (r-l+1)-max(count.values())>k: #window length - max of count values in the hash map that can contain upto 26            
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
        