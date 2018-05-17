import math
class LinearEquation:
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.__d = 0
        self.__e = 0
        self.__f = 0
    
    def getA(self,a):
        self.__a = a
    
    def getB(self,b):
        self.__b = b
    
    def getC(self,c):
        self.__c = c
    
    def getD(self,d):
        self.__d = d
    
    def getE(self,e):
        self.__e = e
    
    def getF(self,f):
        self.__f = f
    
    def isSolvable(self):
        return( (self.__a*self.__d) - (self.__b*self.__c) )
    
    def getX(self):
        return( ((self.__e*self.__d) - (self.__b*self.__f)) / ((self.__a*self.__d) - (self.__b*self.__c)))
    
    def getY(self):
        return( ((self.__a*self.__f) - (self.__e*self.__c)) / ((self.__a*self.__d) - (self.__b*self.__c)))
