class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
node_1=Node("alekhya")
SL=SLL()
SL.head=node_1
node_2=Node("vidhya")
node_3=Node("11")
node_4=Node("10")
node_1.next=node_2
#print(node_1.next)
node_2.next=node_3
#print(node_2.next)
node_3.next=node_4
#print(node_3.next)
#print(node_4.next)
SL.insert_begining("renu")
SL.display()
'''print(SL.head.data) to display head node"


