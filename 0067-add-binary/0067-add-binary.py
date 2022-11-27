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
        a = a[::-1]
        b = b[::-1]
        #print(a, b)
        #ab = int(a[0]) + int(b[0])
        #print(ab)
        sum = ''
        c = 0
        tempsum = 0
        for i in range(len(a)):
            #print(i, a[i], b[i])
            tempsum = c + int(a[i]) + int(b[i])
            #print('     =',tempsum)
            c = 0
            if tempsum > 1:
                c = 1
                tempsum -= 2
                print("CARRY")
            sum = str(tempsum) + sum
            #print('SUM:', sum)
        if c == 1:
            sum = str(c) + sum 
        return sum
            
        