class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ''
        newCommon = strs[0]
        
        for i in range(1, len(strs)):
            common = newCommon
            newCommon = ''
            for j in range(len(strs[i])):
                if j < len(common) and common[j] == strs[i][j]:
                    newCommon += strs[i][j]
                    print(newCommon)
                else:
                    break
        
        return newCommon
                    
                    