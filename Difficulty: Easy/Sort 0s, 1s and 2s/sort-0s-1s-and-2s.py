class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        count_0 = 0
        count_1 = 0
        count_2 = 0
        
        for num in arr:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1
                
        index = 0
                
        for i in range(count_0):
            arr[index] = 0
            index += 1
            
        for i in range(count_1):
            arr[index] = 1
            index += 1
            
        for i in range(count_2):
            arr[index] = 2
            index += 1
            
        return arr
            


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends