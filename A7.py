# Try to do basic stack operations.(push,pop,peep)

class Stacktest:
    
    def __init__(self):
        self.stack = list()
        self.maxSize = 8
        self.top = 0
    
    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return ("Pushed ", data)
    
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return ("Popped ", item)
       
    
    def size(self):
        return self.top

s = Stacktest()
print(s.push(1))
print(s.push(2))
print(s.push(4))
print(s.push(6))
print(s.push(9))
print("Size ", s.size())    
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.pop())
