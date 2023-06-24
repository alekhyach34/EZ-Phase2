'detecting a loop in CLL'
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
    def loop(self):
        if(self.tail.next==self.head):
            print("loop detected")
CLL=CSLL()
node_1=Node(1)
node_2=Node(2)
node_3=Node(3)
node_4=Node(4)
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
#print(CLL.tail.next)
#print(node_4.next)
CLL.loop()
CLL.display()


