class Stack():

    def __init__(self) -> None:
        '''Initialize an empty stack'''
        self._items = []

    def is_empty(self) -> bool:
        '''Check if the stack is empty'''
        return self._items == []
    
    def push(self,item) -> None:
        '''Push an item onto the stack'''
        self._items.append(item)

    def pop(self):
        '''Pop an item off the stack'''
        return self._items.pop()
    
    def peek(self):
        '''Return the top item on the stack'''
        return self._items[-1]
    
    def size(self):
        return len(self._items)