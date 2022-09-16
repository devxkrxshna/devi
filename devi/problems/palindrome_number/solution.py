class Solution(object):
    def isPalindrome(self, x):
        string=str(x)
        if string==string[::-1]:
            return True
        return False
        