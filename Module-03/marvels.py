#class
class Avanger:
    def fight(self):
        print("Avangers start fighting")

 #object
ironman=Avanger() 
hulk=Avanger()

ironman.fight()
hulk.fight()

#introducing method
#class
class Avanger:
    def introduce(self,name):
        print(f"I am {name} and i protect the world")

 #object
ironman=Avanger()
thor=Avanger()
ironman.introduce("Tony")
thor.introduce("Thor")



#default constructor
class Averger:
    def __init__(this):
        print("A new avenger join in this team")
captain=Averger()


#parameterized constructor
class Avanger:
    def __init__(self,name,power):
         self.name=name
         self.power=power
    
    def show(self):
        print(f"{self.name} has power: {self.power}")
        
input_x=input("Enter name :")
spiderman=Avanger(input_x,"web-sliging")
spiderman.show()

#inheritance

class Hero:    #parent class
    def __init__(self,name):
            self.name=name
    
    
    def protect(self):
        print("Protecting the world")
        
class Ironman(Hero):  #child class
    def Fly(self):
        print(f"{self.name} Flying in the sky")
        
tony=Ironman("Ironman")
tony.protect()
tony.Fly()