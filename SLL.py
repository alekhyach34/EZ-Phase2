class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
node_1=Node("alekhya")
SL=SLL()
SL.head=node_1
node_2=Node("vidhya")
node_3=Node("11")
node_4=Node("10")
node_1.next=node_2
print(node_1.next)
node_2.next=node_3
print(node_2.next)
node_3.next=node_4
print(node_3.next)
print(node_4.next)

