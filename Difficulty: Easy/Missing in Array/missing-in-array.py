#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        expect_sum = 0
        for i in range(1,n+1):
            expect_sum += i
            
        actual_sum = sum(arr)
        
        missing_element = expect_sum - actual_sum
        
        return missing_element
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends