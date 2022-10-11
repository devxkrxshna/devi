class Solution(object):
    def reverse(self, n):
        if n<0: sign=-1
        else: sign=1
        abs_n=abs(n)
        res=sign*int(str(abs_n)[::-1])
        if -(2**31)-1 < res < 2**31:
            return res
        else:
            return 0
        