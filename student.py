# student.py
# 
# Class to store info for one student; similar to program on p. 327


class Student:
    def __init__ (self, lastName, firstName, idNum, grades):
        self.firstName = firstName
        self.lastName = lastName
        self.id = idNum
        # make a list for all the HW grades
        self.hwGrade = []
        for i in range (5):
            self.hwGrade.append (grades [i])    # deep copy of grades list
     
    # the following methods allow access to the class's data members
    def getLastName (self):
        return self.lastName
    
    def getName (self):
        return self.lastName + ", " + self.firstName
    
    def getId (self):
        return self.id
        
    def getGrades (self):
        return self.hwGrade