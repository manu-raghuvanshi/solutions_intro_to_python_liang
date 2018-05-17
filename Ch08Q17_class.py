#(The Point class) Design a class named Point to represent a point with x- and ycoordinates.
#The class contains:
#■ Two private data fields x and y that represent the coordinates with get methods.
#■ A constructor that constructs a point with specified coordinates with default point (0, 0).
#■ A method named distance that returns the distance from this point to another point of the Point type.
#■ A method named isNearBy(p1) that returns true if point p1 is close to this 
#point. Two points are close if their distance is less than 5.
#■ Implement the __str__ method to return a string in the form (x, y).

class Point:
    def __init__(self):
        self.__x1 = 0.0
        self.__y1 = 0.0
        self.__x2 = 0.0
        self.__y2 = 0.0
    
    def getX(self,x1,y1):
        self.__x1 = x1
        self.__y1 = y1
        
    def getY(self,x2,y2):
        self.__x2 = x2
        self.__y2 = y2
    
    def distance(self):
        return (((self.__x2 - self.__x1)**2) + ((self.__y2 - self.__y1)**2)) ** 0.5
    
    def isNearBy(self,distance):
        if distance > 5:
            return False
        else:
            return True