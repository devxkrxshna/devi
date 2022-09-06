class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.rstrip()[::-1].split()[0])
