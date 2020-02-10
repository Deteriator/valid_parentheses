class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f"Node: {self.data}")

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('This stack is empty')
        current = self.top
        self.top = current.next
        self.count -= 1
        return current.data

    def peek(self):
        return self.top.data

    def size(self):
        return self.count
        
def valid_parentheses(string):
    stack = Stack()
    pairs = {")": "(",
            "}": "{",
            "]": "["}
    for sym in string:
        if(sym in ["(", "{", "["]):
            stack.push(sym)
        elif (stack.size() == 0 or pairs[sym] != stack.pop()):
            return False

    return True
        