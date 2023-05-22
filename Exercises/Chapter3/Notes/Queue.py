class Queue:
    
    def __init__(self) -> None:
        '''Create a new queue'''
        self._items = []

    def is_empty(self):
        '''Check if the queue is empty'''
        return not bool(self._items)
    
    def enqueue(self,item):
        '''Add a item to the queue'''
        self._items.insert(0,item)

    def dequeue(self):
        '''Remove item of the queue'''
        self._items.pop()
    
    def size(self):
        '''Get the number of items in the queue'''
        return len(self._items)
