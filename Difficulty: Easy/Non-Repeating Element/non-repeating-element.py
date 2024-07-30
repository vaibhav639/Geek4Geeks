#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        for num in arr:
            if freq[num] == 1:
                return num
        return 0
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

for _ in range(0, int(input())):
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr))

# } Driver Code Ends