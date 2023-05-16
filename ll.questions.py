class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def append(self,value):
        new_node=Node(value)
        if  self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1
        return True
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
#Q) find middle value of linked list without using legnth function.  
 #   def middle_element(self):
 #       fast=self.head
  #      slow=self.head

   #     while fast is not None and fast.next is not None:
    #        slow=slow.next
     #       fast=fast.next.next
      #  return slow

#Q2 Find loops in a linked list
    #def loopFinder(self):
     #   fast=self.head
      #  slow=self.head

       # while fast is not None and fast.next is not None:
        #    slow=slow.next
         #   fast=fast.next.next
          #  if fast==slow:
           #     return True
        #return False
    


#mylinked_list1=Linked_list(1)
#mylinked_list1.append(2)
#mylinked_list1.append(3)
#mylinked_list1.append(4)
#mylinked_list1.tail.next=mylinked_list1.head
##print(mylinked_list1.loopFinder())

#mylinked_list2=Linked_list(1)
#mylinked_list2.append(2)
#mylinked_list2.append(3)
#mylinked_list2.append(4)
#print(mylinked_list2.loopFinder())

#Q3 Write a code to remove duplicate elements in a linked list

    def remove_duplicates(self):
        values=set()
        previous=None
        current=self.head
        while current:
            if current.value in values:
                previous.next=current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous=current
            current=current.next

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

    def ll(self,k):
        temp=self.head
        for i in range(k):
            temp=temp.next
        return temp.value 
    
    

#mylinked_list1=Linked_list(1)
#mylinked_list1.append(2)
#mylinked_list1.append(3)
#mylinked_list1.append(4)
#mylinked_list1.append(2)
#mylinked_list1.append(5)
#mylinked_list1.remove_duplicates()
#mylinked_list1.print_list()


#Q4 FInd the kth node from the end .
mylinked_list1=Linked_list(1)
mylinked_list1.append(2)
mylinked_list1.append(3)
mylinked_list1.append(4)
mylinked_list1.append(2)
mylinked_list1.append(5)
mylinked_list1.reverse()
mylinked_list1.print_list()
mylinked_list1.ll(3)
#mylinked_list1.print_list()

      