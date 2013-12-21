class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
        return self.items == []

     def push(self, item):
        self.items.append(item)

     def pop(self):
        return self.items.pop()

     def peek(self):
        return self.items[len(self.items)-1]

     def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


