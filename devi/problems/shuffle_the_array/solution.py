class Solution(object):
    def shuffle(self, nums, n):
        newNums=[]
        j=n
        for i in range(0,n):
            newNums.append(nums[i])
            newNums.append(nums[j])
            j+=1      
        return newNums
        