stack=[]
def push_element():
    if len(stack)==n:
        print("stack is full")
    else:
        e=input()
        stack.append(e)
        print(stack)
def pop_element():
    if not stack:
        print("stack is empty,add the element")
    else:
        element=stack.pop()
        print(element,"removed")
n=int(input())
while True:
    print("select the choice 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter the correct choice")