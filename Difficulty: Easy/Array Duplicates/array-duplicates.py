
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        emp = {}
        
        for num in arr:
            if num in emp:
                emp[num] += 1
            else:
                emp[num] = 1
        duplicate = []
        
        for num,count in emp.items():
            if count > 1:
                duplicate.append(num)
        
        
        if not duplicate:
            return [-1]
            
        duplicate.sort()
        return duplicate
        
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends