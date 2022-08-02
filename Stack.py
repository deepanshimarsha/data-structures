class stack:
    def __init__(self, items):
        self.lst = items

    def add(self, item):
        self.lst.append(item)
    
    def remove(self):
        self.lst.pop()
    
    def peek(self):
        return self.lst[-1]

    def print_stack(self):
        return self.lst

obj = stack([1,2,3,4,5,6])
print(obj.print_stack())
obj.remove()
obj.add(7)
print(obj.print_stack())

    

