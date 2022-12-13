class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        indices={}
        for idx,num in enumerate(sorted(nums)):
            indices.setdefault(num,idx)
        return [indices[num] for num in nums]
        