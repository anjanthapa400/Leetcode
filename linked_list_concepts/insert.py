
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Methods to insert at the beginning of the node
    def push(self,new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Methods to insert the element after certain elements

    def insertAfter(self,prev_data,new_data):

        new_node = Node(new_data)

        temp = self.head
        while (temp):
            if temp.data == prev_data:
                connector = temp.next
                temp.next = new_node
                new_node.next = connector
            temp = temp.next


    #Methods to insert the element at the end 

    def insertAtEnd(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            new_node.next = None

        temp =self.head
        while(temp):
            if temp.next == None:
                temp.next = new_node
                new_node.next = None
            temp = temp.next 

    
    #Method to delete a given key
    def delete_node(self,d_data):

        #store head node

        temp = self.head

        #If first node itself is node to be deleted 

        if (temp is not None):
            if temp.data == d_data:
                self.head = temp.next 
                temp = None
                return
    
        #If the d_data has to be searched on the linked_list then

        while(temp):
            if (temp.data == d_data):
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next
        temp = None

    #Method to delete a given key at a specific position


    def delete_node_position(self,position):
        
        # specify the head of the node

        temp = self.head
        index = 0

        # If the position is at index 0 

        if position == 0:
            if temp == None:
                print("There is no linked list available")


            #print("entered here")

            self.head = self.head.next
            return self.head

        #If the position is to be iterated

        while(temp):
            if (index == position):
                break
            prev = temp
            temp = temp.next 
            index +=1

        prev.next = temp.next 
        temp = None


    # This code includes to detect loop in a linked list

    def detect_loop(self):
        container = []
        temp = self.head

        while(temp):
            if temp.data in container:
                print("There is a loop")

            else:
                container.append(temp.data)

            temp = temp.next


        



llist = LinkedList()
llist.head = Node(1)
second = Node(2)
thrid = Node(3)

llist.head.next = second
second.next = thrid

#llist.print_list()
#llist.push(0)
#llist.print_list()
llist.insertAfter(2,10)
llist.insertAtEnd(25)
llist.push(10)
llist.delete_node_position(1)
llist.print_list()
llist.detect_loop()





