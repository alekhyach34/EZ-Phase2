queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input()
        queue.append(element)
        print(queue)
def dequeue():
    if not queue:
        print("queue is empty,add the element")
    else:
        element=queue.pop(0)
        print(element,"removed")
        print(queue)
n=int(input())
while True:
    print("select the the choice 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter correct choice")