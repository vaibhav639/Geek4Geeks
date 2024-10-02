#User function Template for python3
class Solution:
	def removeVowels(self, S):
		# code here
		vowels = "aeiouAEIOU"
		
		new_s = ""
		
		for char in s:
		    if char not in vowels:
		        new_s += char
		        
		return new_s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends