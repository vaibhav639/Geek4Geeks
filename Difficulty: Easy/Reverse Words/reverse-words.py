# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        S2 = ""
        
        word = S.split(".")
        reverserd_word = word[::-1]
        
        S2 = ".".join(reverserd_word)
        
        return S2
                    
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends