from operator import truediv


class Node :
    def __init__(self,value):
         self.value=value
         self.next=None
class Linked_list :
    def __init__ (self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail=new_node
        self.length=1
    
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node =Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1
#myLinkedList=Linked_list(2)
#myLinkedList.append(5)
#myLinkedList.print_list()
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.tail
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
            return temp
    
# myLinkedList=Linked_list(4)
#myLinkedList.append(9)
#myLinkedList.append(88)
#myLinkedList.print_list()
#myLinkedList.pop()
#myLinkedList.print_list() """

#prepend
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp

    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert (self,index,value):
        if index<0 or index >self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None 
        if index ==0:
            return self.popfirst()
        if index ==self.length-1:
            return self.pop()
        pre = self.get(index -1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp   
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before = None
        for i in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
             

mylinked_list=Linked_list(34)
mylinked_list.append(45)
mylinked_list.append(46)


print(mylinked_list.mi())







        
