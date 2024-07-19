from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        concat_len = word_len * num_words
        word_count = Counter(words)
        result = []
        
        # Iterate over each possible starting point
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    
                    # If there are more occurrences of the word than needed, move the left pointer
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len
                    
                    # Check if the window is valid
                    if right - left == concat_len:
                        result.append(left)
                else:
                    # Reset window if the word is not in the words list
                    current_count.clear()
                    left = right
        
        return result