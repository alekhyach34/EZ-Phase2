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
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
node_1=Node("alekhya")
SL=SLL()
SL.head=node_1
node_2=Node("vidhya")
node_3=Node("11")
node_4=Node("10")
node_1.next=node_2
node_2.next=node_3
node_3.next=node_4
SL.delete_end()
SL.display()





