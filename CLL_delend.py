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
    def delete_begining(self):
        if self.head is None:
            print("CLL is not existing")
        else:
            temp=self.head
            self.head=temp.next
            self.tail.next=self.head
            temp.next=None
    def delete_end(self):
        temp1=self.head.next#current node
        prev=self.head
        while temp1.next!=self.head:
            temp1=temp1.next
            prev=prev.next
        temp1.next=None
        self.tail=prev
        self.tail.next=self.head
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
CLL.delete_end()
CLL.display()




