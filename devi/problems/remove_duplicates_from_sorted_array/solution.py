class Solution(object):
    def removeDuplicates(self, arr):
        a=0
        b=1
        if not arr:
            return 0
        else:
            while b<len(arr):
                if arr[a]==arr[b]:
                    b+=1
                else:
                    a+=1
                    arr[a],arr[b]=arr[b],arr[a]
                    b+=1
            return a+1
        