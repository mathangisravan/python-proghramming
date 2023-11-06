class Node():                                     # Creates a node by taking data from user
    def __init__(self,data):
        self.data = data
        self.link = None

class LinkedList():                               # Class to implement the Linked list
    def __init__(self):                           # Head is created and points to None
        self.head = None
    def add_start(self,data):                     # Element will be added at the beginning of the link
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node
    def display(self):                            #All the data prosent in the nodes will be printed
        n = self.head
        if n == None:                             # check whether the head is pointing any node or not
            print("List is empty!")
        else:
            while n != None:
                print(n.data,"-->",end = " ")
                n = n.link
    def add_end(self,data):                        #Element will be added at the end of the list
        new_node = Node(data)
        if self.head == None:                      #Check whether head is pointing any node or not  
            self.head = new_node
        else:
            n = self.head
            while n.link != None:
                n = n.link
            n.link = new_node
    def add_after(self,data,x):                  #Add an eliment after given value
        n = self.head
        while n !=  None:
            if x == n.data:
                break
            n = n.link
        if n == None:
            print("Node is not present in the LinkedList")
        else:
            new_node = Node(data)
            new_node.link = n.link
            n.link = new_node
    def insert_empty(self,data):              # Add element to empty list
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")
    def add_before(self,data,x):              # Add an element before given value
        if self.head == None:
            print("Linked List is Empty")
            return 
        if self.head.data == x:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.link is not None:
            if self.head.link.data == x:
                break
            n = n.link
        if n.link == None:
            print("Node is not Found in the LinkedList")
        else:
            new_node = Node(data)
            new_node.link = n.link
            n.link = new_node
    def del_first(self):
        if self.head == None:
            print("List is empty!")
        else: 
            self.head == self.head.link



list1 = LinkedList()
list1.add_start(5)
list1.add_end(6)
list1.display()
list1.del_first()
list1.display()







        




#Add this comment#Add this comment