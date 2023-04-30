class Parent(object):
    a = "parent"
    def __init__(self, a="parent_init"):
        self.a = a

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a


class Child(Parent):
    def __init__(self, a="child_init"):

        super().__init__(a)
        # Child.a = "class_a"
        self.a = "class_a"
        print()

if __name__ == "__main__":
    new_obj = Child("main_init")
    print(new_obj.a)
    new_obj.set_a("new_main")
    print(new_obj.get_a())