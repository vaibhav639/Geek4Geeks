#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        dic = {}
        
        for num in A:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        for num,val in dic.items():
            if dic[num] >  N//2:
                return num
            
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends