#User function Template for python3

class Solution:
    def getPairsCount(self, arr, sum):
        from collections import defaultdict
    
    # Dictionary to store frequency of each element
        freq = defaultdict(int)
        count = 0
    
        for num in arr:
            complement = k - num
        
        # Check if complement exists in freq dictionary
            if complement in freq:
                count += freq[complement]
        
        # Update frequency of the current number
            freq[num] += 1
    
        return count
            
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())

    while tc > 0:
        k = int(input().strip())
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.getPairsCount(arr, k)
        print(ans)

        tc -= 1

# } Driver Code Ends