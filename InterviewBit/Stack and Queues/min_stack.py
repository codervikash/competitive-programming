"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : f you are using your own declared global variables, make sure to clear them out in the constructor.
 """

class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
    # @param x, an integer
    def push(self, x):
        self.main_stack.append(x)
        if self.min_stack and self.min_stack[len(self.min_stack) - 1] > x:
            self.min_stack.append(x)
        elif not self.min_stack:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.main_stack):
            popped = self.main_stack.pop()
            if self.min_stack[len(self.min_stack) - 1] == popped:
                self.min_stack.pop()

        return


    # @return an integer
    def top(self):
        if len(self.main_stack):
            return self.main_stack[len(self.main_stack) - 1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if len(self.min_stack):
            return self.min_stack[len(self.min_stack) - 1]
        else:
            return -1
