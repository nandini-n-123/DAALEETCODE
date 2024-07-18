class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count frequencies using a dictionary
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Step 2: Sort elements by frequency in descending order
        sorted_elements = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        
        # Step 3: Return the top k elements
        return sorted_elements[:k]