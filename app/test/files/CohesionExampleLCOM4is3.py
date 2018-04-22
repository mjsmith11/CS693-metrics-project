class CohesionExampleLCOM4is3:

    def __init__(self):
        self.x = 2
        self.y = 3
        self.z = 4
        self.t = 5
        self.u = 6

    def a(self):
        return self.x + self.y

    def b(self):
        return self.y - 2

    def c(self):
        return self.z + 1

    def d(self):
        return self.t - self.z

    def e(self):
        return self.u + 1