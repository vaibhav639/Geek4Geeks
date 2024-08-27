
class Solution:
    def longest(self, names):
        # code here
        if not names:
            return ""  # Return an empty string if the list is empty
    
    # Initialize the longest name with the first element
        longest_name = names[0]
    
    # Iterate over the names starting from the second element
        for name in names[1:]:
        # Update longest_name if the current name is longer
            if len(name) > len(longest_name):
                longest_name = name
    
        return longest_name  # Return the longest name


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        names = input().split()
        obj = Solution()
        res = obj.longest(names)
        print(res)

# } Driver Code Ends