class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items={}
        for i in nums:
            items[i]=items.get(i,0)+1
        print(items)
        for val in items.values():
            if val>1:
                return True
        return False
                
