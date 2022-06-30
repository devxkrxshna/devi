class Solution(object):
    def mostWordsFound(self, sentences):
        lendict={}
        for sentence in sentences:
            lendict[len(sentence.split())]=True
        return max(lendict)    
        