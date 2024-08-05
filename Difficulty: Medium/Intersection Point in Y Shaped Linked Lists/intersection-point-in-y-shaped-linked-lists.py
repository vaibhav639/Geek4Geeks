#User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    temp1 = head1
    temp2 = head2
    diff = 0
    
    if not head1 or not head1.next:
        return -1
        
    if not head2 or not head2.next:
        return -1
    
    L1 = 0
    L2 = 0
    
    while temp1:
        temp1 = temp1.next
        L1+=1
        
    while temp2:
        temp2 = temp2.next
        L2+=1
        
    temp1 = head1
    temp2 = head2
        
    if L1 > L2:
        diff = L1-L2
        for i in range(diff):
            temp1 = temp1.next
            
    else:
        diff = L2 - L1
        for i in range(diff):
            temp2 = temp2.next
            
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1.data
        temp1 = temp1.next
        temp2 = temp2.next
        
    return -1
        
        
        
    
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):

        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(
                    node
                )  # add to the end of the list b, only the intersection

        print(intersetPoint(a.head, b.head))

# } Driver Code Ends