from Ch12Q01_geometric import GeometricObject
class Triangle(GeometricObject):
    def __init__(self,color = "green"):
        super().__init__(color)
        self.side1 = 1.0
        self.side2 = 1.0
        self.side3 = 1.0
        self.s = 0
        self.area = 0
        self.per = 0
    
    def sideOne(self,side1):
        self.side1 = side1
    
    def sidetwo(self,side2):
        self.side2 = side2
    
    def sidethree(self,side3):
        self.side3 = side3
    
    def getArea(self):
        self.s = (self.side1 +self.side2 +self.side3)/2
        print(self.s)
        self.area = (self.s * (self.s - self.side1 ) * (self.s - self.side2) * (self.s - self.side3)) ** 0.5
        print("Area=",self.area)
    
    def getPerimeter(self):
        self.per = self.side1 + self.side2 + self.side3
        print("Perimeter=",self.per)
    
    def __str__(self):
        return super().__str__() + " Triangle: side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)