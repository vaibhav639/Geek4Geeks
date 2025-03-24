#User function Template for python3

class Solution:
    def maxCoins(self, A, B, T, N):
        # code here 
        gold_box = sorted(zip(A,B), key=lambda x:x[1] , reverse = True)
        
        max_coins = 0
        
        for plates,coins in gold_box:
            if T == 0:
                return max_coins
            take_plate = min(T, plates)
            max_coins += take_plate * coins
            T-=take_plate
            
        return max_coins
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        T,N=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxCoins(A,B,T,N))
        print("~")
# } Driver Code Ends