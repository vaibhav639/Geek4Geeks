#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        # Convert strings to sets of unique characters
        setA = set(A)
        setB = set(B)
    
    # Find symmetric difference of both sets
        uncommon_chars = setA.symmetric_difference(setB)
    
    # Sort the characters and join to form the result string
        result = ''.join(sorted(uncommon_chars))
    
    # Return result or "-1" if result is empty
        return result if result else "-1"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends