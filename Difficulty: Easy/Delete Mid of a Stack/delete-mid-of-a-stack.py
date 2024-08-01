#User function Template for python
class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, stack, sizeOfStack):
        temp_stack = []
        mid = sizeOfStack // 2
        count = 0
    
        while count < mid:
            temp_stack.append(stack.pop())
            count += 1
    
    # Remove the middle element
        stack.pop()
    
        while temp_stack:
            stack.append(temp_stack.pop())
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys

sys.setrecursionlimit(10**8)


def main():
    t = int(input())
    while (t > 0):
        sizeOfStack = int(input())
        myStack = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack, sizeOfStack)
        while (len(myStack) > 0):
            print(myStack[-1], end=" ")
            myStack.pop()
        print()
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends