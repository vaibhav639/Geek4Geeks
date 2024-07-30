class Solution:
    def findExtra(self,n,a,b):
        index = -1
        for i in range(0,n-1):
            if index >=0:
                break;
            if a[i]==b[i]:
                pass
            else:
                index = i
                
        return index


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends