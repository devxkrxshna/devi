class Solution(object):
    def decompressRLElist(self, nums):
        ree=[]
        for i in [n for n in range(len(nums)) if n%2==0]:
            res=nums[i:2+i]
            for i in range(res[0]):
                ree.append(res[1])
        return ree
            