import math
class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0 ):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    
    def getN(self):
        return self.__n
    
    def getSide(self):
        return self.__side
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getPerimeter(self):
        return self.__n * self.__side
    
    def getArea(self):
        return (self.__n * math.pow(self.__side,2)) / (4 * math.tan(math.pi /self.__n))

    def getPrint(self):
        print("Area of Polygon with n=",self.__n,"Perimeter=",self.getPerimeter(),"is",self.getArea())
