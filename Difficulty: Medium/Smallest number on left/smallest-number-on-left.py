# User function Template for Python3

class Solution:
    def leftSmaller(self, n, arr):
        stack  = []
        result = []
        
        for num in arr:
            while stack and stack[-1] >= num:
                stack.pop()
                
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
                
            stack.append(num)
            
        return result
                
            
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends