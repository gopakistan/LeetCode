class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        startPoint = 0
        maxVol = 0
        volume = 0
        str1 = ''
        str2 = ''
        str3 = ''
        """
        for i in range(1, len(height)):
            print("test: min(" + str(height[i]) + "||" + str(height[startPoint]) + ")*" + str(i - startPoint))
            volume = (i - startPoint) * (min(height[startPoint], height[i]))
            print("volume = " + str(volume))
            if volume > maxVol:
                maxVol = volume
                print("\tupdated: maxvol = " + str(maxVol))
            if height[i] > height[startPoint]:
                startPoint = i
                print("\t\tupdated start =" +  str(i) +  "; height of" + str(height[startPoint]))
                    
        """

        left = 0
        right = len(height) - 1
        i = 0
        adv = 1
        #for i in range(0, len(height)//2):
        while(right != left):
            #print(str(left) + "<-left | right->" + str(right))
            #print(str(height[left]) + "<-left | right->" + str(height[right]))            
            volume = min(height[left], height[right]) * (right-left)
            #print(str(volume))
            if volume > maxVol:
                maxVol = volume
            if(height[left] > height[right]):
                right -= 1
            else:
                left += 1
         
        return maxVol
