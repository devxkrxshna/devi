class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        product=1
        for i,num in enumerate(nums):
            if i-1==-1:
                res.append(1)
            else:
                product=product*nums[i-1]
                res.append(product)
        product=1
        for i in reversed(range(len(nums))):
            if i+1==len(nums):
                res[-1]=res[-1]*1
            else:
                product=product*nums[i+1]
                res[i]=product*res[i]
        return res