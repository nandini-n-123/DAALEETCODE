class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        to_remove = k
        
        for digit in num:
            while to_remove > 0 and stack and stack[-1] > digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        
        # Remove remaining digits to meet the requirement of removing k digits
        while to_remove > 0:
            stack.pop()
            to_remove -= 1
        
        # Construct the result ignoring leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Handle case where result is empty, return '0'
        return result if result else '0'