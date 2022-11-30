class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = len(digits)-1
    
        while digits[k] == 9:
            digits[k] = 0
            k -= 1
            if k == -1:
                digits.insert(0, 1)

        if k != -1:
            digits[k] = digits[k] + 1
        return digits