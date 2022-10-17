class Solution(object):
    def isSubsequence(self, s, t):
        slow=0
        for c in t:
            if slow==len(s):break
            if c==s[slow]:
                slow+=1
        return slow==len(s)
            
        