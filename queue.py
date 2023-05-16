from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queueu:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def Printq(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=None
            self.last=None
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1

    def dequeu(self):
        if self.first is None:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=self.first.next
            self.length-=1
            return temp

MeraQueue=Queueu(32)
MeraQueue.enqueue(92)
MeraQueue.dequeu()

MeraQueue.Printq()