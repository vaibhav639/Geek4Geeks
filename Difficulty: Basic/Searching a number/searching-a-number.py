
from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        for index, value in enumerate(arr):
            if value == k:
                # Return 1-based index
                return index + 1
        # If no match was found, return -1
        return -1
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        k = int(input())  # Read the element to search
        arr = list(map(int, input().split()))  # Read the array elements

        obj = Solution()
        res = obj.search(k, arr)

        print(res)

# } Driver Code Ends