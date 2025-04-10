
class Solution:
    def countWays(self, n):
        
        if n == 0 or n == 1 or n == 2:
            return n
    
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2  # Base cases
    
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]  


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends