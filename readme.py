class Solution(object):
    def ToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        codes = "holamund12345IJKLMNOPQRSTUVWXYZ"
        res   = ""
         do
            n    = n - 1
            res  += codes[ n%26 ]
            n    //= 26
        return res[::-1]
