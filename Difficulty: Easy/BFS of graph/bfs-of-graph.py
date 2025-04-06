#User function Template for python3
from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        start = 0
        result = []
        queue = deque([start])
        visited = set([start])
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in adj[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    
        return result
            

#{ 
 # Driver Code Starts
import sys
from queue import Queue
from typing import List


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends