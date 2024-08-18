from collections import deque
class Solution:
    def minSum(self, arr, n):
        arr = sorted(arr)
        dq = deque(arr)
        Numstrng1 = ""
        Numstrng2 = ""
        
        
        if n == 0:
            return 0
        if n == 1:
            return dq.popleft()
            
        while dq:
            firstpop = dq.popleft()
            Numstrng1 += str(firstpop)
            if dq:
                secondpop = dq.popleft()
                Numstrng2 += str(secondpop)
            else:
                break
            
            
        Minsumm = int(Numstrng1) + int(Numstrng2)
        return Minsumm
        
        
    


#{ 
 # Driver Code Starts
import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends