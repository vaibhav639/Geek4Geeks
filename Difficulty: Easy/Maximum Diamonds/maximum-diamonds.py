#User function Template for python3
import heapq
class Solution:
    def maxDiamonds(self, A, N, K):
        max_heap = [-x for x in A]
        heapq.heapify(max_heap)
        
        total_diamond = 0
        
        for i in range(K):
            if not max_heap:
                break
            
            max_diamond_in_bag = -heapq.heappop(max_heap)
            total_diamond += max_diamond_in_bag
            remaining_diamond = max_diamond_in_bag // 2
            heapq.heappush(max_heap , -remaining_diamond)
            
        return total_diamond
            
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends