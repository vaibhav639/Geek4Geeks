#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        actual_sum = n * (n+1) // 2
        arr_sum = 0
        for i in arr:
            arr_sum = arr_sum + i
        missing_num = actual_sum - arr_sum
        return missing_num
        
        
             
             
        


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