class Solution(object):
    def isAnagram(self, s, t):
        dict_s={}
        dict_t={}
        for i in s:
            if i not in dict_s:
                dict_s[i]=1
            else:
                dict_s[i]+=1
        for c in t:
            if c not in dict_t:
                dict_t[c]=1
            else:
                dict_t[c]+=1
        return dict_s==dict_t
        
        