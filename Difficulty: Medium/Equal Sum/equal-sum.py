#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

	def equilibrium(self,arr): 
    	# code here
        n = len(arr)
        left = [0] * (n)
        right = [0] * (n)

        left[0] = 0
        right[-1] = 0
        i = 0

        for i in range(1,n):
            left[i] = left[i-1] + arr[i-1]
    
        for j in range(n-2,-1,-1):
            right[j] = right[j+1] + arr[j+1]


        for i in range(len(left)):
            if left[i] == right[i]:
                return "true"
        return "false"

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.equilibrium(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends