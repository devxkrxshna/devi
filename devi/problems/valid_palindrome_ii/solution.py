class Solution(object):
    def validPalindrome(self,str):
        head=0
        tail=len(str)-1
        while head<tail:
            if str[head]!=str[tail]:
                del_head_str=str[head:tail] #delete the character at the tail pointer
                del_tail_str=str[head+1:tail+1] # delete the character at the head pointer and includes the character at the tail pointer
                return del_head_str==del_head_str[::-1] or del_tail_str==del_tail_str[::-1]
            head+=1
            tail-=1
        return True
        
        