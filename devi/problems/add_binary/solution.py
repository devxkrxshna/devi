class Solution(object):
    def addBinary(self, a, b):
        a=list(a)
        b=list(b)
        carry=0
        res=[]
        while a or b or carry:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())
            res.append(str(carry%2))
            carry=carry//2
        return "".join(res[::-1])
        