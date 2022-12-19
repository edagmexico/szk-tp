class Solution(object):
    def ToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
<<<<<<< HEAD
        codes = "ABCDEFGHIJKLMNOPSDGANBSDGIUlguksdfQRSTUVWXYZ"
=======
        codes = "holamund12345IJKLMNOPQRSTUVWXYZ"
>>>>>>> c146368574ab5c76b77dabf588da2db835fadda2
        res   = ""
         do
            n    = n - 1
            res  += codes[ n%26 ]
            n    //= 26
        return res[::-1]
