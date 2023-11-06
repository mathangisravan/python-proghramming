class Node():
    def __init__(self,data) :
        self.data= data
        self.link = None

class Linkedlist(): 
    def __init__(self):  
        self.head = None

node1 = Node(5)
node2 = Node(6)


List1 = Linkedlist()
List1.head = node1
node1.link = node2

if node1.link.link == None:
    node1.link = None

else:
    print("Bye")
print(node1.link)
