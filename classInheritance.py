
class Parent:
    parent_Attr = 100
    def __init__(self):
        print("Calling parent constructor")

    def my_Method(self):
        print("Calling parent method")

    def set_Attr(self, attr):
        Parent.parent_Attr = attr

    def get_Attr(self):
        print("Parent attribute", Parent.parent_Attr)

class Child(Parent):
    def my_Method(self):
        print("Calling child constructor")

    def child_Method(self):
        print("Calling child method")

c = Child()
c.child_Method()
c.my_Method()
c.set_Attr(200)
c.get_Attr()