#User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        chars_to_remove = set(string2)
    
    # Construct the result string by filtering out characters found in string2
        result = ''.join([char for char in string1 if char not in chars_to_remove])
    
        return result
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()
        
        ob = Solution()
        print(ob.removeChars(string1,string2))
# } Driver Code Ends