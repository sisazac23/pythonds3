import Node

class UnorderedList:

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

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
            current = current.next
        
        return False
    
    def remove(self, item):
        current = self.head
        previous = None

        while current != None:
            if current.data == item:
                break
            previous = current
            current = current.next
        
        if current == None:
            raise ValueError('Item not found')
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next