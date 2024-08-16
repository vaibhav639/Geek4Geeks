# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self, arr, n):
        # Handle the case when the array has only one element
        if n == 1:
            return 0
        
        # Check if the first element is a peak
        if arr[0] >= arr[1]:
            return 0
        
        # Check if the last element is a peak
        if arr[n - 1] >= arr[n - 2]:
            return n - 1
        
        # Iterate through the internal elements
        for i in range(1, n - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i
        
        # In case no peak is found, although with the given conditions, 
        # this line should not be reached.
        return -1




#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends