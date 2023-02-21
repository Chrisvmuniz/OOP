import random
import time
from datetime import date

class Student:

    def __init__(self,ID,Name,Month,Day,Year,Class):
        self.StudentID = ID
        self.Name = Name
        self.DOB = [Month,Day,Year]
        self.Classification = Class
                 
     


    def StudentShowSelf(self):
        print (self.StudentID,self.Name,self.DOB,self.Classification) 
    
    def CurrentAge(self):
        today = date.today()
        todaysYear = today.year
        todaysMonth = today.month
        todaysDay= today.day
       
        #age = todaysYear - int(self.DOB[2])
        return(self.DOB.index())


    def StudentRegistration(self):
        if self.Classification == "Senior":
            print("Seniors 4/1 - 4/3")
        elif self.Classification == "Junior":
            print("Juniors 4/4 - 4/6")
        elif self.Classification == "Sophmore":
            print("")
        elif self.Classification == "Freshman":
            print("")
        #Sophmores 4/7 - 4/9
        #Freshman 4/10 - 4/12
    
   
        

