#(The Time class) Design a class named Time
import time
class Time:
    def __init__(self):
        self.__today=time.time()%(3600*24)
        self.__hour=0
        self.__minutes=0
        self.__second=0
    
    def getHour(self):
        self.__hour= int(self.__today//(60*60))
        return self.__hour
    
    def getMinutes(self):
        self.__minutes=int((self.__today%(60*60))//60)
        return self.__minutes
        
    def getSecond(self):
        self.__second=int(self.__today%60)
        return self.__second
    
    def setTime(self,elapseTime):
        self.__today = elapseTime%(3600*24)
        print("Current Time is",self.getHour(),":",self.getMinutes(),":",self.getSecond())