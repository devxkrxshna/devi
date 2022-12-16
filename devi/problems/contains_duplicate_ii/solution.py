class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        item={}
        for i,num in enumerate(nums):
            if num in item and abs(item[num]-i)<=k:
                return True
            item[num]=i
        return False