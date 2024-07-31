#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        freq_a = {}
        freq_b = {}
        
        if len(a)!=len(b):
            return False
            
        for char in a:
            if char in freq_a:
                freq_a[char] += 1
            else:
                freq_a[char] = 1
        
        for char in b:
            if char in freq_b:
                freq_b[char] += 1
            else:
                freq_b[char] = 1
            
        
        if freq_a == freq_b:
            return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends