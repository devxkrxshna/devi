class Solution(object):
    def runningSum(self, nums):
        sumlist=[]
        sums=0
        for i in nums:
            sums=sums+i
            sumlist.append(sums)
        return sumlist