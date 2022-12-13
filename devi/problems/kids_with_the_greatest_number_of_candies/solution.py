class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res=[]
        maxCandie=max(candies)
        for i in candies:
            res.append((i+extraCandies)>=maxCandie)
        return res
        