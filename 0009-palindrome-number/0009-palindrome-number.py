class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x1 = str(x)[0:len(str(x))//2]
        x2 = str(x)[::-1][0:len(str(x))//2]
        
        if x1 == x2:
            return True
        else:
            return False
        