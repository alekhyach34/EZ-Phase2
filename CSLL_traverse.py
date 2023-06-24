class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("Circular list is empty")
        else:
            temp=self.head
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data)
CLL=CSLL()
node_1=Node("cholleti")
node_2=Node("alekhya")
node_3=Node("vidhya")
CLL.head=node_1
CLL.tail=node_1
CLL.tail.next=CLL.head
node_1.next=node_2
CLL.tail=node_2
CLL.tail.next=CLL.head
node_2.next=node_3
CLL.tail=node_3
CLL.tail.next=CLL.head
print(CLL.tail.next)
print(node_3.next)
CLL.display()


