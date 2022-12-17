class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht={}
        for i,num in enumerate(nums):
            if target-num in hasht:
                return [hasht[target-num],i]
            else:
                hasht[num]=i
        return [-1,-1]