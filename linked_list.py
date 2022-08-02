class Node:
    def __init__(self, data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self, item_values):
        self.lst = item_values
        self.head = Node(self.lst[0])
        self.length = len(self.lst)

    def create(self):
        ptr = self.head
        for i in range(1,self.length):
            ptr.next = Node(self.lst[i])
            ptr = ptr.next

    def print(self):
        l = []
        ptr = self.head
        while ptr:
            l.append(ptr.data)
            ptr = ptr.next

        return l

    def remove(self, pos):
        ptr = self.head
        if pos == 1:
            self.head = ptr.next
            ptr.next = None
        else:
            while pos-1  > 0:
                ptr = ptr.next
                pos = pos - 1
        
            ptr2 = ptr.next
            ptr.next = ptr2.next
            ptr2.next = None

    def add(self,pos,item_val):
        new_node = Node(item_val)
        ptr = self.head
        if pos == 1:
            new_node.next = ptr
            self.head = new_node
        else:
            while pos-1 > 0:
                ptr = ptr.next
                pos = pos-1
        
            new_node.next = ptr.next
            ptr.next = new_node
    
    
            



        



            
 

        