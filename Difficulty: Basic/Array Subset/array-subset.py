#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freq_a = {}
        freq_b = {}
        
        for num in a:
            freq_a[num] = freq_a.get(num,0) + 1
        for num in b:
            freq_b[num] = freq_b.get(num,0) + 1
            
        for key,val in freq_b.items():
            if key in freq_a:
                if val > freq_a[key]:
                    return False
            else:
                return False
        return True
            
        
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends