# This solution includes leetcode problem for find the middle of the linked list 


class ListNode:
    
    def __init__(self, val=0, next = None):

        self.val = val
        self.next = next

class Solution:

    def middleNode(self,head):

        l = len(head)

        self.head = None

        for i in head[::-1]:
            new_node = ListNode(i)
            new_node.next = self.head
            self.head = new_node

        
        one_step = self.head
        two_step = self.head
        
        while(two_step and two_step.next):
            one_step = one_step.next
            two_step = two_step.next.next

        print("one_step",one_step.val)

        while(one_step):
            print(one_step.val)
            one_step = one_step.next


    
    def printlist(self):
        current = self.head

        while(current):
            print(current.val)
            current = current.next


llist = Solution()
llist.middleNode([1,2,3,4,5,6])
