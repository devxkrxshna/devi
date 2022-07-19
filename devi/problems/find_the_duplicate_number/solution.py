class Solution(object):
    def findDuplicate(self, a):
        hasht={}
        count=1
        for i in range(len(a)):
            if a[i] not in hasht:
                hasht[a[i]]=count
            else:
                hasht[a[i]]=count+1
                if hasht[a[i]]==2:
                    break
        return a[i]