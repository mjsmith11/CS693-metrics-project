class CouplingExample1:

    def __init__(self):
        self.otherClass = CouplingExample2()
        pass

    def n1(self):
        self.otherClass.m1()
        self.otherClass.m3()

    def n2(self):
        pass

    def n3(self):
        self.otherClass.m2()

    def n4(self):
        pass

class CouplingExample2:

    def __init__(self):
        self.otherClass = CouplingExample1()
        pass

    def m1(self):
        self.otherClass.n1()

    def m2(self):
        pass

    def m3(self):
        self.otherClass.n4()