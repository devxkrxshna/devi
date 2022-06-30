class Solution(object):
    def maximumWealth(self, accounts):
        sumsofcust={}
        for cust in accounts:
            sumsofcust[sum(cust)]=True
        return max(sumsofcust)
        