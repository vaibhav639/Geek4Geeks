#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        freq = {}
        n = len(arr)
        
        for num in arr:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
                
        for num,count in freq.items():
            if count > n//2:
                return num
                
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends