class Solution(object):
    def numIdenticalPairs(self, arr):
        dict={}
        count=0
        for i in arr:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for key,value in dict.items():
            combination=value*(value-1)//2
            count+=combination
        
        return count
        
        