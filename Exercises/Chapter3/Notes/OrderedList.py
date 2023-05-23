import Node

class OrderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        
        while current != None:
            count += 1
            current = current.next
        
        return count
    
    def search(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False
    
    def add(self,item):
        current = self.head
        previous = None
        temp = Node(item)
        
        while current != None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp
