# User function Template for python3

class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        l = len(arr)
        
        if l == 0:
            return -1
        if l == 1:
            return 1
            
        totalSum = sum(arr)
        leftSum = 0
        
        for i in range(l):
            rightSum = totalSum - leftSum - arr[i]
            
            if leftSum == rightSum:
                return i + 1
            leftSum += arr[i]
        return -1
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.equilibriumPoint(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends