class Solution(object):
    def titleToNumber(self,str):
        str=str.upper()
        summ=0
        power=1
        for i in reversed(range(len(str))):
            digit=ord(str[i])-64
            summ+=power*digit
            power=power*26
        return summ
        