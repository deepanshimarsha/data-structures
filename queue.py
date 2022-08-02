class queue:
    def __init__(self, items):
        self.lst = items

    def enqueue(self,item):
        self.lst.insert(0,item)

    def dequeue(self):
        self.lst.pop()

    def front(self):
        return self.lst[-1]
    
    def rear(self):
        return self.lst[0]

    def print_queue(self):
        return self.lst

obj = queue([1,2,3,4,5,6])
obj.dequeue()
obj.enqueue(10)
print(obj.print_queue())
print(obj.rear())
