class Solution(object):
    def reverseString(self, s):
        head=0
        tail=len(s)-1
        while(head<tail):
            s[head],s[tail]=s[tail],s[head] #swapping elements
            head+=1
            tail-=1
        return s