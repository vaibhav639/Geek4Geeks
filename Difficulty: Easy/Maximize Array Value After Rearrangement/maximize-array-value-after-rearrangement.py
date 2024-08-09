#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        summ = 0
        arr = sorted(arr)
        n = len(arr)
        
        for i in range(n):
            summ += i*arr[i]
        MOD = 10**9 + 7
        
        return summ % MOD



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends