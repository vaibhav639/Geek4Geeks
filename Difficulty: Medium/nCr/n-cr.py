#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        num = 1
        dum = 1
        for i in range(1,r+1):
            num = num * n
            dum = dum * i
            n-=1
        return num//dum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends