class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to count frequencies of characters
        char_count = {}
        
        # Count frequencies of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Initialize length of longest palindrome
        length = 0
        odd_found = False
        
        # Calculate length of longest palindrome
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        # Add 1 if there was any character with odd frequency
        if odd_found:
            length += 1
        
        return length