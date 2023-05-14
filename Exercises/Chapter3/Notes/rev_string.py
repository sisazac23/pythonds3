import Stack

def rev_string(mystr):
    '''This function uses a Stack to reverse a string'''

    m = Stack()
    for s in mystr:
        m.push(s)
    to_r = []
    for s in mystr:
        to_r.append(m.pop())
    return ''.join(to_r)

def rev_str(mystr):

    m = Stack()
    for s in mystr:
        m.push(s)
    reversed = ''
    while not m.is_empty():
        reversed += m.pop()
    return reversed