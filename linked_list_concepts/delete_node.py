# This solution includes the leetcode problems for deleting a node from linked list 


from calendar import c


class Node:

    def __init__(self,data):
        self.data = data 
        self.next = None


class Solution:

    def deleteNode(self,node,box):

        self.head = None

        for chunks in box[::-1]:
            new_node = Node(chunks)
            new_node.next = self.head
            self.head = new_node
        
        current = self.head 

        while(current):
            if (current.data == node):
                break
            prev = current    
            current = current.next 

        print(current.data)
        while(current.next is not None):
            print("entered")
            current.data =current.next.data
            current.next = current.next.next






    
    def print_linkedlist(self):

        temp = self.head 

        while(temp):
            print(temp.data)
            temp = temp.next 


llist = Solution()
llist.deleteNode(3,[1,2,3,4,5])
llist.print_linkedlist()
        



