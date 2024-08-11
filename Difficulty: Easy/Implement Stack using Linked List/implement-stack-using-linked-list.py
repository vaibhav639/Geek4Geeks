class MyStack:


    class StackNode:

    # Constructor to initialize a node
        def __init__(self, data):
            self.data = data
            self.next = None
        
        
    def __init__(self):
        self.top = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        
    #Function to remove an item from top of the stack.
    def pop(self):
        if self.top == None:
            return -1
        else:
            pop = self.top.data
            self.top = self.top.next
            return pop
            

        # Add code here



#{ 
 # Driver Code Starts
class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()

# } Driver Code Ends