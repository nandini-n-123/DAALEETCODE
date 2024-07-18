class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        # Initialize dp array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to stay on the ground (do nothing)
        dp[1] = 1  # There's one way to reach the first step (1 step)
        
        # Compute dp values from 2 to n
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]