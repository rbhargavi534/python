class Parent:
    def disp(self):
        print("parent")

class Child(Parent):
     def disp(self):
        print("Child")
    

c1=Child()
c1.disp()