#User function Template for python3

class Solution:
	def countOddEven(self, arr):
        # Initialize counters for odd and even numbers
        odd_count = 0
        even_count = 0

        # Iterate through the array and count odd and even numbers
        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        # Return the count of odd and even elements as an array
        return [odd_count, even_count]
		


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr)

        # Printing the result
        print(*res)

# } Driver Code Ends