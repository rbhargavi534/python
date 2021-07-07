class Parent:
    def __init__(self):
        print("parent cons")

class Child(Parent):
     def __init__(self):
         super().__init__()
         print("Child cons")
    

c1=Child()
