class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        runflag = 0
        for i in range(len(nums)):
            if nums[i] == target and runflag == 0:
                first = i
                runflag = 1
            if nums[i] != target and runflag == 1:
                print(nums[i])
                last = i-1
                break
        if first != -1 and last == -1:
            last = len(nums)-1
        return([first,last])
                    
        