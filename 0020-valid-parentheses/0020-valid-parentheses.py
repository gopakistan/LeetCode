class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        check = 0
        
        for i in s:
            if i == '(':
                stack.append(1)
            elif i == '[':
                stack.append(2)
            elif i == '{':
                stack.append(3)
            elif len(stack) == 0:
                return False
            elif i == ')':
                check = stack[len(stack)-1]
                if check != 1:
                    return False
                else:
                    stack = stack[:len(stack)-1]
            elif i == ']':
                check = stack[len(stack)-1]
                if check != 2:
                    return False
                else:
                    stack = stack[:len(stack)-1]
            elif i == '}':
                check = stack[len(stack)-1]
                if check != 3:
                    return False
                else:
                    stack = stack[:len(stack)-1]
        if len(stack) == 0:
            return True
        return False
        
        