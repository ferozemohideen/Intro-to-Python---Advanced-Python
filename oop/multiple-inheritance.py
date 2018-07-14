class ClassA:
    def hi(self):
        print("Hello!")

class ClassB:
    def hi(self):
        print("Hallo!")

class ClassC(ClassA, ClassB):
    pass

c = ClassC()
c.hi() #will print ClassA "Hello!" because it is first