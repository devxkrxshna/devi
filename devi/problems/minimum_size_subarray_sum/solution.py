class Solution(object):
    def minSubArrayLen(self, target, arr):
        slow=0
        subArrSum=0
        res=float('inf')
        for fast in range(len(arr)):
            subArrSum+=arr[fast]
            while subArrSum>=target:
                res=min(res,fast-slow+1)
                subArrSum-=arr[slow]
                slow+=1
        return 0 if res==float('inf') else res
        