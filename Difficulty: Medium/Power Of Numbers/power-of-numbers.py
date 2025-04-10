#User function Template for python3

class Solution:
    def reverse_exponentiation(self, n):
        # code here
        power = int(str(n)[::-1])
# print(reverse)
        result = n
        while power-1:
            result = result*n
            power-=1
        return result

#{ 
 # Driver Code Starts
# Input handling
if __name__ == "__main__":
    T = int(input())  # test cases

    for _ in range(T):
        n = int(input())  # input N
        solution = Solution()
        ans = solution.reverse_exponentiation(n)
        print(ans)

# } Driver Code Ends