class Solution(object):
    def maxProfit(self, arr):
        profit=0
        slow=0
        fast=1
        while fast<len(arr):
            if arr[slow]<arr[fast]:
                profit=max(profit,arr[fast]-arr[slow])
            else:
                slow=fast
            fast+=1
        return profit
      