import time

class Node:

    def __init__(self, data=None):
        '''initialize node with data and next pointer'''
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        """initialize stack stack pointer"""
        print('Stack created')
        self.stack_pointer = None

    def push(self, x):
        """add x to the top of the stack"""
        if not isinstance(x, Node):
            x = Node(x)
        print(f"Adding {x.data}) to the top of the stack")
        if self.is_empty():
            self.stack_pointer = x
        else:
            x.next = self.stack_pointer
            self.stack_pointer = x

    def pop(self):
        """remoe and return the node on top of the stack"""
        if not self.is_empty():
            print(f"Removing node on top of stack")
            curr = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            curr.next = None
        else:
            return "Stack is empty"

    def is_empty(self):
        """return True if stack is empty, else return false"""
        return self.stack_pointer == None

    def peek(self):
        """look at the node on top of the stack"""
