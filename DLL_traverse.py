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
node_1=Node("alekhya")
DL=DLL()
DL.head=node_1
node_2=Node("vidhya")
node_3=Node("reddy")
node_4=Node("renu")
node_5=Node("cholleti")
#print(node_1.data)#node data
#print(DL.head)'address of head node'
#print(DL.head.data)#head node data
node_1.next=node_2
node_2.prev=node_1
#print(node_1.next)
#print(node_1)
node_2.next=node_3
node_3.prev=node_2
#print(node_2.next)
#print(node_2)
node_3.next=node_4
node_4.prev=node_3
#print(node_3.next)
#print(node_3)
node_4.next=node_5
node_5.prev=node_4
#print(node_4.next)
#print(node_4)
node_5.next=None
#print(node_5.next)
#print(node_5)
DL.display()

