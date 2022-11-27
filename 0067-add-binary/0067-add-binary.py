class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ''
        
        while (len(a) > len(b)):
            b = '0' + b
        while (len(a) < len(b)):
            a = '0' + a
            
        sum = ''
        c = 0
        tempsum = 0
        for i in range(len(a)-1, -1, -1):
            tempsum = c + int(a[i]) + int(b[i])
            c = 0
            if tempsum > 1:
                c = 1
                tempsum -= 2
            sum = str(tempsum) + sum
            
        if c == 1:
            sum = str(c) + sum 
        return sum
            
        