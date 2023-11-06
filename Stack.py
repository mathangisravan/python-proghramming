from collections import deque
class stack:
    def __init__(self):
        self.k = deque()
    def push(self,n):
        self.k.append(n)
    def pop(self):
        print(self.k.pop())
    def display(self):
        print(self.k)
    def peak(self):
        print(self.k[-1])

stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.display()
stack1.peak()
stack1.pop()
class queue :
    def __init__(self):
        self.k = deque()
    def push(self,n):
        self.k.appendleft(n)

