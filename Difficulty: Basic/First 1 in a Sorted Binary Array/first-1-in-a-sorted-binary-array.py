#{ 
 # Driver Code Starts

# } Driver Code Ends
#User function Template for python3

class Solution:
    def firstIndex(self, arr):
        low, high = 0, len(arr) - 1
        result = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Check if mid is the first occurrence of 1
            if arr[mid] == 1:
                result = mid  # Store the potential result
                high = mid - 1  # Move left to find an earlier occurrence
            else:
                low = mid + 1  # Move right if the mid element is 0
        
        return result
    # Your code goes here



#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.firstIndex(arr))
    
# } Driver Code Ends