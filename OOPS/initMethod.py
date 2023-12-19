# Init method

class InitMethod:
    def __init__(self):
        # init method will be pointing to the same object as the s1 method
        self.name = "Nitin"
        self.rollno = 45

# creating an object
s1 = InitMethod()
s2 = InitMethod()

#  they will be pointing to the same object
print(s1.__dict__)
print(s2.__dict__)

# both are at different address but they are pointing to the same object
print(s1, s2)


class Demo:
    def Market():
        s1