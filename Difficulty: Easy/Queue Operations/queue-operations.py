from collections import deque
class Solution:
    # Function to insert element into the queue
    def insert(self, q, k): 
        dq = deque(q)
        dq.append(k)
        

    def findFrequency(self, q, k):
        dq = deque(arr)
        freq = {}
        
        for num in dq:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
        if k in freq:
            return freq[k]
        else:
            return -1
        

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        obj = Solution()
        q = []
        n = int(input())
        arr = list(map(int, input().strip().split()));
        for k in arr:
            obj.insert(q,k)
        
        
        m = int(input())
        query = list(map(int, input().strip().split()));
        for k in query:
            f = obj.findFrequency(q,k)
            if f!=0:
                print(f)
            else:
                print(-1)

# } Driver Code Ends