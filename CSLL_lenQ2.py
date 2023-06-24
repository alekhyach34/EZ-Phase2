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
    def countNodes(self):
        temp = self.head#1. create a temp node pointing to head
        count = 0#2. create a variable to count nodes
        if (temp != None):#3. if the temp node is not null increase
            count += 1#   i by 1 and move to the next node, repeat
            temp = temp.next #   the process till the temp becomes null
            while (temp != self.head):
                count += 1
                temp = temp.next
            print(count)#4. return the count
        
    
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
CLL.countNodes()
CLL.display()



