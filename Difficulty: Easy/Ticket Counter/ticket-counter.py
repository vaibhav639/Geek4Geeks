from collections import deque
class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        dq = deque(range(1, N + 1))

        if len(dq) == K:
            return dq.pop()

        flag = False
        while len(dq) > K:
            x = K
            flag = False
            while len(dq) > x and x != 0:
                dq.popleft()
                x -= 1

            x = K
            while len(dq) > x and x != 0:
                dq.pop()
                x -= 1
                flag = True

        if flag:
            return dq.pop()
        return dq.popleft()


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends