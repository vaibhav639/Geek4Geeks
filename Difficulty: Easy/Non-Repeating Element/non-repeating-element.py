#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        freq = {}

        for num in arr:
            freq[num] = freq.get(num,0) + 1
            
        for key,val in freq.items():
            if val == 1:
                return key
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

for _ in range(0, int(input())):
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr))

    print("~")

# } Driver Code Ends