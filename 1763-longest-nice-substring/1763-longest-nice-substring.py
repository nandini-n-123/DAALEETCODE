class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(sub):
            # Set to track lowercase and uppercase characters found
            lower_set = set()
            upper_set = set()
            
            for char in sub:
                if char.islower():
                    lower_set.add(char)
                elif char.isupper():
                    upper_set.add(char)
                    
            # Check if for every lowercase character, there exists an uppercase counterpart
            # and vice versa
            for char in lower_set:
                if char.upper() not in upper_set:
                    return False
            
            for char in upper_set:
                if char.lower() not in lower_set:
                    return False
            
            return True
        
        def find_longest_nice(s):
            n = len(s)
            longest = ""
            
            # Iterate through all possible substrings
            for i in range(n):
                for j in range(i + 1, n + 1):
                    substring = s[i:j]
                    if is_nice(substring) and len(substring) > len(longest):
                        longest = substring
            
            return longest
        
        return find_longest_nice(s)