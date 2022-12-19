class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        codes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res   = ""
        while n:
            n    = n - 1
            res  += codes[ n%26 ]
            n    //= 26
        return res[::-1]
