class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = 0
        ite = 1
        while (root + ite <= x):
            root += ite
            ite += 2
            
        return ite//2
        