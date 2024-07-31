#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    stack = []
    
    for char in S:
        stack.append(char)
        
    revString = ""
    
    while stack:
        revString += stack.pop()
        
    return revString
        

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends