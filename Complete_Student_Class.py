class Student:
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getRollNumber(self):
        return self.__RollNumber
    
    def setRollNumber(self, RollNumber):
        self.__RollNumber=RollNumber
    
obj1 = Student()
obj1.setName("Amogh")
print("Name:", obj1.getName())
obj1.setRollNumber(7590)
print("Roll Number:", obj1.getRollNumber())