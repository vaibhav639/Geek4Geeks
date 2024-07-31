#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		S2 = ""
		for char in S[::-1]:
		    S2 += char
		if S == S2:
		    return 1
		else:
		    return 0
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends