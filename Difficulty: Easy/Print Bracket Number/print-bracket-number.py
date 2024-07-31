#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
	    list = []
	    stack  = []
	    count = 0
	    
	    for char in str:
	        if char == "(":
	            count = count + 1
	            stack.append(count)
	            list.append(count)
	        elif char == ")":
	            popElement = stack.pop()
	            list.append(popElement)
	            
	    return list
	            
	           
	            
	            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends