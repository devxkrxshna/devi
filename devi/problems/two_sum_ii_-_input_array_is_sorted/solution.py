class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hasht={}
        for i,num in enumerate(numbers):
            if target-num in hasht:
                return [hasht[target-num]+1,i+1]
            hasht[num]=i
        return [-1,-1]
