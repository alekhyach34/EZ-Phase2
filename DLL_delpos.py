class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<==>",end=" ")
                temp=temp.next
    def delete_position(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
node_1=Node("alekhya")
DL=DLL()
DL.head=node_1
node_2=Node("vidhya")
node_3=Node("reddy")
node_4=Node("renu")
node_1.next=node_2
node_2.prev=node_1
node_2.next=node_3
node_3.prev=node_2
node_3.next=node_4
node_4.prev=node_3
DL.delete_position(2)
DL.display()



