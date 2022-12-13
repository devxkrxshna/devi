class Solution(object):
    def decode(self, encoded, first):
        res=[first]
        for i in range(len(encoded)):
            res.append(res[i]^encoded[i])
        return res