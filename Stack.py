class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack():
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height==None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
    def pop (self):
        if self.height==None:
            return None
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
        self.height-=1
        return temp


MeraStack=Stack(23)
MeraStack.push(24)
MeraStack.push(25)
MeraStack.pop()
MeraStack.print_stack()
