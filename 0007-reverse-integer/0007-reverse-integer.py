class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(-1*x)[::-1])
            x *= -1
        if abs(x) < pow(2,31) - 1:
            return x
        else:
            return 0