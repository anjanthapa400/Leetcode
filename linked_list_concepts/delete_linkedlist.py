class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:

    #Initializing the linked list 

    def __init__(self):
        self.head = None


    def push(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    
    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next 

    
    def delete_linkedlist(self):

        current = self.head
        print("entered here")

        while(current):
            prev = current.next

            del current.data

            current = prev

        self.head = None


    def length_of_linkedlist(self):

        temp = self.head
        count = 0

        while(temp):
            count +=1
            temp = temp.next

        return count

    # Program to find the nth node from the last of the linked list

    def nodeFromLast(self,val):

        current = self.head
        temp = self.head
        count = 0
        while(current):
            count +=1
            current = current.next
        print("count",count)
        for i in range(0,(count-val-1)):
            temp  = temp.next

        print(temp.data)



llist = Linkedlist()
llist.printlist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printlist()
print("length of a linked list is {}".format(llist.length_of_linkedlist()))

llist.nodeFromLast(2)
