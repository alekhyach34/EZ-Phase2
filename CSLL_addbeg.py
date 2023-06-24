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
    def insert_begining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            self.tail.next=new_node
            new_node.next=self.head
    def insert_position(self,pos,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            if pos==1:
                insert_begining(data)
            else:
                  temp=self.head
                  for i in range(1,pos-1):#prev pos is having temp
                    temp=temp.next
                  new_node.next=temp.next
                  temp.next=new_node
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
#print(CLL.tail.next)
#print(node_3.next)
#CLL.insert_begining("giri")
#CLL.insert_end("pooja")
CLL.insert_position(3,"renu")
CLL.display()



