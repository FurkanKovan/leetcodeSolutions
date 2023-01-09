# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/min-stack/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

# (1) The stack is created by using linked list approach
# Create a Node class that points to the value of itself and the next value that comes after it
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# (2) The Stack class itself is created under this 'MinStack' class to make an appropriate submission
# This MinStack class represents both a Stack (that will hold the actual values given) and a MinStack (that will hold
# only the last minimum value given)
# A stack(the MinStack) is used to represent these minimum values because if a pop() operation is made, 
# the tracking of the minimum value is still preserved. 
# Create a MinStack class that has the "init, push, pop, top, getMin" methods (structure is already given by the problem)
class MinStack:

    # (3) The self.head and self.minStackHead hold the top values of the Stack and MinStack, respectively
    # When created since there has been no value added yet, they point to None
    def __init__(self):
        self.head = None # stack
        self.minStackHead = None # minStack
    
    # (4) The MinStack is going to be an additional stack that will record the last minimum value that has been added
    # to the Stack(that holds the actual values)
    # Whenever a value is provided, it is directly added to the Stack, but for minStack first a comparison is made,
    # between the provided value and the MinStack's top value(minStackHead)
    def push(self, val:int) -> None:
        # If the Stack is empty create the first Node for Stack and MinStack
        if self.head == None:
            self.head = Node(val)
            self.minStackHead = Node(val)
        else:
            # If Stack is not empty add the value in a linked list style (Node.next points to the head and
            # the head becomes the newNode)
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            # For MinStack the operation is the same but only the minimum value is added between the provided value and
            # the MinStack's top value. This top value always holds the very last minimum value
            val = min(val, self.minStackHead.data)
            newMinStackNode = Node(val)
            newMinStackNode.next = self.minStackHead
            self.minStackHead = newMinStackNode
    
    # (5) A pop operation made in a linked list style for both the Stack and the MinStack
    def pop(self) -> None:
        # If the stack is empty dont bother
        if self.head == None:
            return None
        else:
            # First pop() is made from minStack since the actual popped value from Stack is returned at the end
            # MinStack
            poppedNode = self.minStackHead
            self.minStackHead = self.minStackHead.next
            # Stack
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            return poppedNode.data

    # (6) Return the Stack's head value, that is the Node.data
    def top(self) -> int:
        return self.head.data

    # (7) Return the MinStack's head value, that is the Node.data
    def getMin(self) -> int:
        return self.minStackHead.data
 