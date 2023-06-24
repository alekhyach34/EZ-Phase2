class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
CLL=CSLL()
node_1=Node("cholleti")
node_2=Node("alekhya")
node_3=Node("vidhya")
node_4=Node("renu")
node_5=Node("giri")
node_6=Node("pooja")
#print(node_1)
#print(node_1.data)
#print(node_2)
#print(node_3)
#CLL.tail=node_1
#CLL.tail.next=CLL.head#tail.next-->address of head node-->head node tail node both are same((for single node))
CLL.head=node_1
CLL.tail=node_1
CLL.tail.next=CLL.head
node_1.next=node_2
CLL.tail=node_2
CLL.tail.next=CLL.head
node_2.next=node_3
CLL.tail=node_3
CLL.tail.next=CLL.head
node_3.next=node_4
CLL.tail=node_4
CLL.tail.next=CLL.head
node_4.next=node_5
CLL.tail=node_5
CLL.tail.next=CLL.head
node_5.next=node_6
CLL.tail=node_6
CLL.tail.next=CLL.head
print(CLL.tail.next)
print(node_6.next)

