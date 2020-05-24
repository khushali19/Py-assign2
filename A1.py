# W.A.P to demonstrate class concepts along with constructor and destructor.


class demo:
    
    def __init__(self):
        print("I am in constructor .. ")
        
        
    def cube(self,x):
        self.x = x
        c = x**3
        print("Cube is ", c)
        
    def __del__(self):
        print("I am in destructor .. ")
        
obj = demo()
obj.cube(9)