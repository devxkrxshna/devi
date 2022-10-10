class Solution(object):
    def isPalindrome(self, s):
        cleaned=[i.lower() for i in s if i.isalnum()]
        return cleaned==cleaned[::-1]
        