class Solution(object):
    def containsDuplicate(self, arr):
        dictt={}
        for i in arr:
            if i not in dictt:
                dictt[i]=1
            else:
                return True
        return False