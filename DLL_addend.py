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
    def insert_begining(self,data):
        new_node=Node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
            if temp.next is None:
                temp.next=new_node
                new_node.prev=temp
            new_node.next=None
    def insert_position(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
node_1=Node("alekhya")
DL=DLL()
DL.head=node_1
node_2=Node("vidhya")
node_3=Node("reddy")
node_4=Node("cholleti")
node_1.next=node_2
node_2.prev=node_1
node_2.next=node_3
node_3.prev=node_2
node_3.next=node_4
node_4.prev=node_3
DL.insert_position(2,"renu")
DL.display()




