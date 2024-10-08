#User function Template for python3
import string
class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        if len(s) < 26:
            return False
            
        stack = []
        
        all_alphabets = set(string.ascii_lowercase)
        
        for char in s:
            if char.isalpha():
                char = char.lower()
                
                if char not in stack:
                    stack.append(char)
            
                
            if len(stack) == 26:
                return True
            
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends