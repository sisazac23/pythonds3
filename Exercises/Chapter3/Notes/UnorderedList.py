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

        
    def append(self, item):
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.next
        
        temp = Node(item)
        previous.next = temp

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0

        while count != pos:
            previous = current
            current = current.next
            count += 1
        
        temp = Node(item)
        previous.next = temp
        temp.next = current
    
    def index(self, item):
        current = self.head
        count = 0

        while current != None:
            if current.data == item:
                return count
            current = current.next
            count += 1
        
        return -1
    
    def pop(self, pos=None):
        current = self.head
        previous = None
        count = 0

        if pos == None:
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            return current.data
        else:
            while count != pos:
                previous = current
                current = current.next
                count += 1
            previous.next = current.next
            return current.data